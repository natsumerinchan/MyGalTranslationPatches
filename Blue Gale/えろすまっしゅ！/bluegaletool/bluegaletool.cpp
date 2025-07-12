#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <filesystem>
#include <algorithm>
#include <iomanip>
#include <cctype>
#include <unordered_map>

// 添加Windows头文件
#ifdef _WIN32
#include <windows.h>
#endif

namespace fs = std::filesystem;

// 类型定义
typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;
typedef signed char s8;

#pragma pack(push, 1)
struct zbm_header_t {
    s8 magic[4];        // "amp_"
    u16 version;        // must be 0x0001
    u32 uncomprlen;
    u32 data_offset;    // >= 14
};

struct inx_header_t {
    u32 index_entries;
};

struct inx_entry_t {
    s8 name[64];
    u32 offset;
    u32 length;
};
#pragma pack(pop)

// 解压缩函数
static unsigned int zbm_decompress(u8* uncompr, unsigned int uncomprlen,
    u8* compr, unsigned int comprlen) {
    unsigned int curbyte = 0;
    unsigned int curbit = 1;
    unsigned int act_uncomprlen = 0;
    u8 copy_bytes;
    unsigned int i;

    auto getbit_be = [](unsigned char byte, unsigned int pos) {
        return !!(byte & (1 << (7 - pos)));
    };

    while (true) {
        copy_bytes = 0;
        for (i = 0; i < 8; i++) {
            copy_bytes <<= 1;
            copy_bytes |= getbit_be(compr[curbyte], curbit++);
            if (curbit == 8) {
                curbit = 0;
                curbyte++;
                if (curbyte == comprlen)
                    goto out;
            }
        }

        if (copy_bytes & 0x80) {
            unsigned int offset;
            copy_bytes &= ~0x80;
            offset = 0;
            for (i = 0; i < 10; i++) {
                offset <<= 1;
                offset |= getbit_be(compr[curbyte], curbit++);
                if (curbit == 8) {
                    curbit = 0;
                    curbyte++;
                    if (curbyte == comprlen)
                        goto out;
                }
            }

            for (i = 0; i < copy_bytes; i++) {
                if (act_uncomprlen >= uncomprlen)
                    goto out;
                uncompr[act_uncomprlen] = uncompr[act_uncomprlen - offset];
                act_uncomprlen++;
            }
        }
        else {
            for (i = 0; i < copy_bytes; i++) {
                u8 data = 0;
                for (unsigned int k = 0; k < 8; k++) {
                    data <<= 1;
                    data |= getbit_be(compr[curbyte], curbit++);
                    if (curbit == 8) {
                        curbit = 0;
                        curbyte++;
                        if (curbyte == comprlen)
                            goto out;
                    }
                }

                if (act_uncomprlen >= uncomprlen)
                    break;
                uncompr[act_uncomprlen++] = data;
            }
        }
    }
out:
    return act_uncomprlen;
}

// 处理 .zbm 文件
bool process_zbm(const fs::path& input_path, const fs::path& output_dir) {
    std::ifstream file(input_path, std::ios::binary);
    if (!file) {
        std::cerr << "无法打开文件: " << input_path << std::endl;
        return false;
    }

    // 读取文件头
    zbm_header_t header;
    file.read(reinterpret_cast<char*>(&header), sizeof(header));

    // 验证魔数和版本
    if (memcmp(header.magic, "amp_", 4) != 0) {
        std::cerr << "无效的ZBM文件: 魔数不匹配" << std::endl;
        return false;
    }

    if (header.version != 1) {
        std::cerr << "不支持的ZBM版本: " << header.version << std::endl;
        return false;
    }

    if (header.data_offset < 14) {
        std::cerr << "无效的ZBM文件: 数据偏移太小" << std::endl;
        return false;
    }

    // 读取压缩数据
    file.seekg(0, std::ios::end);
    size_t file_size = file.tellg();
    size_t comprlen = file_size - header.data_offset;
    file.seekg(header.data_offset, std::ios::beg);

    std::vector<u8> compr_data(comprlen);
    file.read(reinterpret_cast<char*>(compr_data.data()), comprlen);
    file.close();

    // 解压缩数据
    std::vector<u8> uncompr_data(header.uncomprlen);
    unsigned int act_uncomprlen = zbm_decompress(uncompr_data.data(), header.uncomprlen,
        compr_data.data(), comprlen);

    if (act_uncomprlen != header.uncomprlen) {
        std::cerr << "解压缩失败: 解压后大小不匹配 (" 
                  << act_uncomprlen << " vs " << header.uncomprlen << ")" << std::endl;
        return false;
    }

    // 特殊处理：如果前两个字节是 0xBD 0xB2，则对前64字节取反
    if (uncompr_data.size() >= 2 && uncompr_data[0] == 0xBD && uncompr_data[1] == 0xB2) {
        for (size_t k = 0; k < std::min<size_t>(64, uncompr_data.size()); k++) {
            uncompr_data[k] = ~uncompr_data[k];
        }
    }

    // 创建输出文件
    fs::path output_path = output_dir / (input_path.stem().string() + ".bmp");
    std::ofstream out_file(output_path, std::ios::binary);
    if (!out_file) {
        std::cerr << "无法创建输出文件: " << output_path << std::endl;
        return false;
    }

    out_file.write(reinterpret_cast<const char*>(uncompr_data.data()), uncompr_data.size());
    out_file.close();

    std::cout << "成功提取: " << output_path << " (" 
              << uncompr_data.size() << " 字节)" << std::endl;
    return true;
}

// 处理 .bdt 文件
bool process_bdt(const fs::path& input_path, const fs::path& output_dir) {
    std::ifstream file(input_path, std::ios::binary);
    if (!file) {
        std::cerr << "无法打开文件: " << input_path << std::endl;
        return false;
    }

    // 读取整个文件
    file.seekg(0, std::ios::end);
    size_t file_size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<u8> data(file_size);
    file.read(reinterpret_cast<char*>(data.data()), file_size);
    file.close();

    // 对每个字节取反
    for (size_t i = 0; i < data.size(); i++) {
        data[i] = ~data[i];
    }

    // 创建输出文件
    fs::path output_path = output_dir / (input_path.stem().string() + ".txt");
    std::ofstream out_file(output_path, std::ios::binary);
    if (!out_file) {
        std::cerr << "无法创建输出文件: " << output_path << std::endl;
        return false;
    }

    out_file.write(reinterpret_cast<const char*>(data.data()), data.size());
    out_file.close();

    std::cout << "成功提取: " << output_path << " (" 
              << data.size() << " 字节)" << std::endl;
    return true;
}

// BDT回封功能（从TXT生成BDT）
bool repack_bdt(const fs::path& input_path, const fs::path& output_path) {
    std::ifstream file(input_path, std::ios::binary);
    if (!file) {
        std::cerr << "无法打开文件: " << input_path << std::endl;
        return false;
    }

    // 读取整个文件
    file.seekg(0, std::ios::end);
    size_t file_size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<u8> data(file_size);
    file.read(reinterpret_cast<char*>(data.data()), file_size);
    file.close();

    // 对每个字节取反（回封操作）
    for (size_t i = 0; i < data.size(); i++) {
        data[i] = ~data[i];
    }

    // 创建输出文件
    std::ofstream out_file(output_path, std::ios::binary);
    if (!out_file) {
        std::cerr << "无法创建输出文件: " << output_path << std::endl;
        return false;
    }

    out_file.write(reinterpret_cast<const char*>(data.data()), data.size());
    out_file.close();

    std::cout << "成功回封: " << output_path << " (" 
              << data.size() << " 字节)" << std::endl;
    return true;
}

// 处理 .snn 文件
bool process_snn(const fs::path& input_path, const fs::path& lst_path, const fs::path& output_dir) {
    // 打开数据文件
    std::ifstream data_file(input_path, std::ios::binary);
    if (!data_file) {
        std::cerr << "无法打开数据文件: " << input_path << std::endl;
        return false;
    }

    // 打开索引文件
    std::ifstream lst_file(lst_path, std::ios::binary);
    if (!lst_file) {
        std::cerr << "无法打开索引文件: " << lst_path << std::endl;
        return false;
    }

    // 读取索引头
    inx_header_t header;
    lst_file.read(reinterpret_cast<char*>(&header), sizeof(header));

    // 读取索引条目
    std::vector<inx_entry_t> entries(header.index_entries);
    lst_file.read(reinterpret_cast<char*>(entries.data()), 
                 header.index_entries * sizeof(inx_entry_t));
    lst_file.close();

    std::cout << "在索引文件中找到 " << header.index_entries << " 个资源条目" << std::endl;

    // 处理每个资源
    for (size_t i = 0; i < entries.size(); i++) {
        const auto& entry = entries[i];
        
        // 修复类型问题：将 s8 数组转换为 char 数组
        char name_buffer[65] = {0}; // 64字符+空终止符
        for (size_t j = 0; j < 64; j++) {
            name_buffer[j] = static_cast<char>(entry.name[j]);
        }
        name_buffer[64] = '\0'; // 确保以空字符结尾
        
        // 获取实际文件名长度
        size_t name_len = strnlen(name_buffer, 64);
        std::string name(name_buffer, name_len);
        
        // 确保文件名安全
        for (auto& c : name) {
            if (c == '/' || c == '\\' || c == ':' || c == '*' || c == '?' || 
                c == '"' || c == '<' || c == '>' || c == '|') {
                c = '_';
            }
        }

        // 读取资源数据
        data_file.seekg(0, std::ios::end);
        size_t file_size = data_file.tellg();
        data_file.seekg(0, std::ios::beg);
        
        if (static_cast<size_t>(entry.offset) + static_cast<size_t>(entry.length) > file_size) {
            std::cerr << "资源 " << name << " 超出文件范围" << std::endl;
            continue;
        }

        data_file.seekg(entry.offset, std::ios::beg);
        std::vector<u8> resource_data(entry.length);
        data_file.read(reinterpret_cast<char*>(resource_data.data()), entry.length);

        // 创建输出文件
        fs::path output_path = output_dir / name;
        
        // 创建必要的子目录
        fs::create_directories(output_path.parent_path());
        
        std::ofstream out_file(output_path, std::ios::binary);
        if (!out_file) {
            std::cerr << "无法创建资源文件: " << output_path << std::endl;
            continue;
        }

        out_file.write(reinterpret_cast<const char*>(resource_data.data()), resource_data.size());
        out_file.close();

        std::cout << "提取资源: " << std::setw(40) << std::left << name 
                  << " 大小: " << std::setw(10) << entry.length 
                  << " 字节" << std::endl;
    }

    data_file.close();
    return true;
}

// 显示帮助信息
void show_help() {
    std::cout << "BLUEGALE 资源提取工具 v1.1\n";
    std::cout << "用法:\n";
    std::cout << "  bluegale_tool [选项] <输入文件> [输出目录]\n\n";
    std::cout << "选项:\n";
    std::cout << "  -t, --type <类型>   指定文件类型 (zbm, bdt, snn)\n";
    std::cout << "  -l, --lst <文件>    指定.snn文件的.lst索引文件\n";
    std::cout << "  -r, --repack        回封模式 (BDT专用)\n";
    std::cout << "  -h, --help          显示帮助信息\n\n";
    std::cout << "支持的文件类型:\n";
    std::cout << "  zbm  - 压缩位图文件 (输出为 .bmp)\n";
    std::cout << "  bdt  - 二进制数据文件 (输出为 .txt)\n";
    std::cout << "  snn  - 资源包文件 (需要对应的 .lst 索引文件)\n\n";
    std::cout << "示例:\n";
    std::cout << "  bluegaletool -t zbm image.dat\n";
    std::cout << "  bluegaletool -t snn -l index.lst package.dat output_dir\n";
    std::cout << "  bluegaletool -t bdt scene00.bdt\n";
    std::cout << "  bluegaletool -t bdt -r scene00.txt scene00.bdt\n";
}

// Windows控制台编码设置函数
void set_console_encoding() {
#ifdef _WIN32
    // 设置控制台编码为UTF-8
    SetConsoleOutputCP(65001);
    SetConsoleCP(65001);
    
    // 设置控制台字体以支持UTF-8
    CONSOLE_FONT_INFOEX fontInfo;
    fontInfo.cbSize = sizeof(fontInfo);
    GetCurrentConsoleFontEx(GetStdHandle(STD_OUTPUT_HANDLE), FALSE, &fontInfo);
    wcscpy(fontInfo.FaceName, L"Consolas");
    SetCurrentConsoleFontEx(GetStdHandle(STD_OUTPUT_HANDLE), FALSE, &fontInfo);
#endif
}

// 解析命令行参数
std::unordered_map<std::string, std::string> parse_arguments(int argc, char* argv[]) {
    std::unordered_map<std::string, std::string> args;
    
    // 默认输出目录
    args["output"] = "extracted";
    
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];
        
        // 帮助选项
        if (arg == "-h" || arg == "--help") {
            args["help"] = "true";
            return args;
        }
        
        // 回封模式
        else if (arg == "-r" || arg == "--repack") {
            args["repack"] = "true";
        }
        
        // 文件类型
        else if (arg == "-t" || arg == "--type") {
            if (i + 1 < argc) {
                args["type"] = argv[++i];
            } else {
                std::cerr << "错误: -t 参数需要指定文件类型" << std::endl;
                args["error"] = "true";
                return args;
            }
        }
        
        // .lst 文件
        else if (arg == "-l" || arg == "--lst") {
            if (i + 1 < argc) {
                args["lst"] = argv[++i];
            } else {
                std::cerr << "错误: -l 参数需要指定.lst文件" << std::endl;
                args["error"] = "true";
                return args;
            }
        }
        
        // 输入文件或输出目录
        else {
            if (args.find("input") == args.end()) {
                args["input"] = arg;
            } else if (args.find("output") == args.end()) {
                args["output"] = arg;
            } else {
                std::cerr << "警告: 忽略多余的参数: " << arg << std::endl;
            }
        }
    }
    
    return args;
}

int main(int argc, char* argv[]) {
    set_console_encoding();
    
    // 如果没有参数，显示帮助
    if (argc < 2) {
        show_help();
        return 1;
    }
    
    // 解析命令行参数
    auto args = parse_arguments(argc, argv);
    
    // 检查是否需要显示帮助
    if (args.find("help") != args.end()) {
        show_help();
        return 0;
    }
    
    // 检查是否有错误
    if (args.find("error") != args.end()) {
        return 1;
    }
    
    // 检查输入文件是否存在
    if (args.find("input") == args.end()) {
        std::cerr << "错误: 未指定输入文件" << std::endl;
        show_help();
        return 1;
    }
    
    // 检查回封模式是否支持
    if (args.find("repack") != args.end() && 
        args.find("type") != args.end() && 
        args["type"] != "bdt") {
        std::cerr << "错误: 回封模式目前只支持BDT文件类型" << std::endl;
        return 1;
    }
    
    fs::path input_path(args["input"]);
    fs::path output_dir(args["output"]);
    
    // 确保输出目录存在
    if (!fs::exists(output_dir)) {
        fs::create_directories(output_dir);
    }

    std::cout << "输入文件: " << input_path << "\n";
    std::cout << "输出目录: " << output_dir << "\n\n";

    try {
        // 处理回封模式
        bool repack_mode = (args.find("repack") != args.end());
        if (repack_mode) {
            std::cout << "模式: 回封\n";
        }
        
        // 确定文件类型
        std::string file_type;
        if (args.find("type") != args.end()) {
            file_type = args["type"];
            std::transform(file_type.begin(), file_type.end(), file_type.begin(), 
                          [](unsigned char c){ return std::tolower(c); });
        } else {
            // 从文件扩展名推断类型
            std::string ext = input_path.extension().string();
            if (!ext.empty() && ext[0] == '.') {
                ext = ext.substr(1); // 去掉点号
            }
            std::transform(ext.begin(), ext.end(), ext.begin(), 
                          [](unsigned char c){ return std::tolower(c); });
            file_type = ext;
        }
        
        // 处理不同文件类型
        if (file_type == "zbm") {
            if (repack_mode) {
                std::cerr << "错误: ZBM文件暂不支持回封功能" << std::endl;
                return 1;
            } else {
                if (!process_zbm(input_path, output_dir)) {
                    std::cerr << "提取 .zbm 文件失败" << std::endl;
                    return 1;
                }
            }
        }
        else if (file_type == "bdt") {
            if (repack_mode) {
                // 回封模式：从TXT生成BDT
                fs::path output_path = output_dir;
                if (fs::is_directory(output_dir)) {
                    // 如果输出参数是目录，自动生成文件名
                    output_path /= input_path.stem().string() + ".bdt";
                }
                if (!repack_bdt(input_path, output_path)) {
                    std::cerr << "回封 .bdt 文件失败" << std::endl;
                    return 1;
                }
            } else {
                // 正常模式：从BDT提取TXT
                if (!process_bdt(input_path, output_dir)) {
                    std::cerr << "提取 .bdt 文件失败" << std::endl;
                    return 1;
                }
            }
        }
        else if (file_type == "snn") {
            if (repack_mode) {
                std::cerr << "错误: SNN文件暂不支持回封功能" << std::endl;
                return 1;
            }
            // 确定.lst文件路径
            fs::path lst_path;
            if (args.find("lst") != args.end()) {
                lst_path = args["lst"];
            } else {
                // 自动查找同名的.lst文件
                lst_path = input_path;
                lst_path.replace_extension(".lst");
            }
            
            if (!fs::exists(lst_path)) {
                std::cerr << "找不到索引文件: " << lst_path << std::endl;
                return 1;
            }
            
            std::cout << "使用索引文件: " << lst_path << std::endl;
            
            if (!process_snn(input_path, lst_path, output_dir)) {
                std::cerr << "提取 .snn 文件失败" << std::endl;
                return 1;
            }
        }
        else {
            std::cerr << "不支持的文件类型: " << file_type << std::endl;
            show_help();
            return 1;
        }
    }
    catch (const std::exception& e) {
        std::cerr << "错误: " << e.what() << std::endl;
        return 1;
    }

    std::cout << "\n处理完成!" << std::endl;
    return 0;
}