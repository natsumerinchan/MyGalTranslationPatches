// pkdtool.cpp, v2.0
// coded by asmodean extended by DeepSeek-R1

// 解包：pkdtool.exe -e <input.pkd> -o <output_folder>
// 封包：pkdtool.exe -r <input_folder> -o <output.pkd>

#include <io.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <direct.h>
#include <cerrno>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct PKDHDR {
  unsigned char signature[4]; // "PACK"
  unsigned long entry_count;
};

struct PKDENTRY {
  char          filename[128];
  unsigned long length;
  unsigned long offset;
};

void unobfuscate(unsigned char* buff, unsigned long len, unsigned char key) {
  unsigned char* end = buff + len;
  while (buff < end) {
    *buff++ ^= key;
  }
}

int open_or_die(const string& filename, int flags, int mode = 0) {
  int fd = open(filename.c_str(), flags, mode);
  if (fd == -1) {
    fprintf(stderr, "Could not open %s (%s)\n", filename.c_str(), strerror(errno));
    exit(-1);
  }
  return fd;
}

void make_path(const string& filename) {
  char temp[4096] = {0};
  strncpy(temp, filename.c_str(), sizeof(temp) - 1);
  for (char* p = temp; *p; p++) {
    if (*p == '\\' || *p == '/') {
      char t = *p;
      *p = '\0';
      mkdir(temp);
      *p = t;
    }
  }
}

void make_dir(const string& path) {
    char temp[4096] = {0};
    strncpy(temp, path.c_str(), sizeof(temp)-1);

    char* p = temp;
    while (*p) {
        if (*p == '\\' || *p == '/') {
            char t = *p;
            *p = '\0';
            if (strlen(temp) > 0) {
                _mkdir(temp);
            }
            *p = t;
        }
        p++;
    }
    _mkdir(temp);
}

void extract_pkd(const string& input_pkd, const string& output_folder) {
  int fd = open_or_die(input_pkd, O_RDONLY | O_BINARY);

  PKDHDR hdr;
  read(fd, &hdr, sizeof(hdr));

  unsigned long entries_len = hdr.entry_count * sizeof(PKDENTRY);
  PKDENTRY* entries = new PKDENTRY[hdr.entry_count];
  read(fd, entries, entries_len);

  unsigned char key = entries[0].filename[sizeof(entries[0].filename) - 1];
  unobfuscate(reinterpret_cast<unsigned char*>(entries), entries_len, key);

  // 创建配置文件
  make_dir(output_folder);
  string config_path = output_folder + "/pack.config";
  FILE* config_file = fopen(config_path.c_str(), "wb");
  if (!config_file) {
    fprintf(stderr, "Could not create config file %s\n", config_path.c_str());
    exit(-1);
  }
  fprintf(config_file, "key=0x%02X\n", key);
  for (unsigned long i = 0; i < hdr.entry_count; i++) {
    fprintf(config_file, "%s\n", entries[i].filename);
  }
  fclose(config_file);

  for (unsigned long i = 0; i < hdr.entry_count; i++) {
    unsigned long len = entries[i].length;
    unsigned char* buff = new unsigned char[len];
    lseek(fd, entries[i].offset, SEEK_SET);
    read(fd, buff, len);
    unobfuscate(buff, len, key);

    string out_path = output_folder + "/" + entries[i].filename;
    make_path(out_path);

    int out_fd = open_or_die(out_path, O_CREAT | O_TRUNC | O_WRONLY | O_BINARY, S_IREAD | S_IWRITE);
    write(out_fd, buff, len);
    close(out_fd);

    delete[] buff;
  }

  delete[] entries;
  close(fd);
}

void repack_pkd(const string& input_folder, const string& output_pkd) {
  // 读取配置文件
  string config_path = input_folder + "/pack.config";
  FILE* config_file = fopen(config_path.c_str(), "rb");
  if (!config_file) {
    fprintf(stderr, "Could not open config file %s\n", config_path.c_str());
    exit(-1);
  }

  unsigned char key = 0;
  char line[256] = {0};
  fgets(line, sizeof(line), config_file);
  sscanf(line, "key=0x%02hhX", &key);

  vector<string> filenames;
  while (fgets(line, sizeof(line), config_file)) {
    line[strcspn(line, "\r\n")] = 0; // 去除换行符
    if (line[0]) {
      filenames.push_back(line);
    }
  }
  fclose(config_file);

  vector<PKDENTRY> entries;
  vector<unsigned char*> datas;
  vector<unsigned long> lengths;

  unsigned long offset = sizeof(PKDHDR) + filenames.size() * sizeof(PKDENTRY);

  for (const auto& name : filenames) {
    string full_path = input_folder + "/" + name;
    int fd = open_or_die(full_path, O_RDONLY | O_BINARY);

    struct stat st;
    fstat(fd, &st);
    unsigned long len = st.st_size;
    unsigned char* data = new unsigned char[len];
    read(fd, data, len);
    close(fd);

    unobfuscate(data, len, key);

    PKDENTRY entry = {0};
    strncpy(entry.filename, name.c_str(), sizeof(entry.filename) - 1);
    entry.length = len;
    entry.offset = offset;

    entries.push_back(entry);
    datas.push_back(data);
    lengths.push_back(len);

    offset += len;
  }

  // 处理条目数据
  unsigned long entries_len = entries.size() * sizeof(PKDENTRY);
  unobfuscate(reinterpret_cast<unsigned char*>(entries.data()), entries_len, key);

  // 写入文件头
  PKDHDR hdr = {{'P','A','C','K'}, static_cast<unsigned long>(entries.size())};

  int out_fd = open_or_die(output_pkd, O_CREAT | O_TRUNC | O_WRONLY | O_BINARY, S_IREAD | S_IWRITE);
  write(out_fd, &hdr, sizeof(hdr));
  write(out_fd, entries.data(), entries_len);

  // 写入文件数据
  for (size_t i = 0; i < datas.size(); i++) {
    write(out_fd, datas[i], lengths[i]);
    delete[] datas[i];
  }

  close(out_fd);
}

int main(int argc, char** argv) {
  bool extract = false;
  bool repack = false;
  string input_path;
  string output_path;

  for (int i = 1; i < argc; i++) {
    if (strcmp(argv[i], "-e") == 0 && i + 1 < argc) {
      extract = true;
      input_path = argv[++i];
    } else if (strcmp(argv[i], "-r") == 0 && i + 1 < argc) {
      repack = true;
      input_path = argv[++i];
    } else if (strcmp(argv[i], "-o") == 0 && i + 1 < argc) {
      output_path = argv[++i];
    }
  }

  if (extract && !output_path.empty()) {
    extract_pkd(input_path, output_path);
  } else if (repack && !output_path.empty()) {
    repack_pkd(input_path, output_path);
  } else {
    fprintf(stderr, "Usage:\n"
                    "Unpack: %s -e <input.pkd> -o <output_folder>\n"
                    "Pack:   %s -r <input_folder> -o <output.pkd>\n", 
                    argv[0], argv[0]);
    return -1;
  }

  return 0;
}
