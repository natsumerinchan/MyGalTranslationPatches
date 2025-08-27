#encoding=utf-8
import os
import struct
import re

import bytefile

def parse_cmd(cmd):
    op = cmd & 0xffff
    int_cnt = (cmd & 0xff0000) >> 16
    str_cnt = (cmd >> 24) & 0xf
    unk = cmd >> 28
    return (op, int_cnt, str_cnt, unk)

def parse_name_table(ls):
    names = {}
    pat = re.compile(r'(\d+),\d*,\d*,([^,]+),.*')
    for l in ls:
        mo = pat.match(l)
        if mo:
            names[int(mo.group(1))] = mo.group(2)
    return names

def is_half(s, cp):
    return len(s.decode(cp)) == len(s)

def parse_rld_header(stm):
    magic, unk1, unk2, inst_cnt, unk3 = struct.unpack('<4sIIII', stm.read(20))
    tag = stm.readstr()
    stm.seek(0x114)
    return (magic, unk1, unk2, inst_cnt, unk3, tag)

def decode_with_special(s, cp):
    """解码字符串，但将\xF0\x40序列转换为0xF040表示"""
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        # 检查当前位置是否是\xF0\x40序列的开始
        if i + 1 < n and s[i] == 0xF0 and s[i+1] == 0x40:
            # 如果之前有未解码的字节，先解码它们
            if i > 0:
                try:
                    result.append(s[:i].decode(cp))
                except:
                    # 如果解码失败，直接使用原始字节表示
                    result.append(''.join(f'\\x{b:02X}' for b in s[:i]))
                s = s[i:]
                i = 0
            
            # 添加特殊标记
            result.append('0xF040')
            s = s[2:]  # 跳过\xF0\x40
            n = len(s)
            continue
        
        i += 1
    
    # 处理剩余的字节
    if len(s) > 0:
        try:
            result.append(s.decode(cp))
        except:
            result.append(''.join(f'\\x{b:02X}' for b in s))
    
    return ''.join(result)

def parse_rld(stm, name_table, cp):
    txt = []
    pure_txt = []
    magic, h_unk1, h_unk2, inst_cnt, h_unk3, h_tag = parse_rld_header(stm)
    
    if magic != b'\0DLR':
        raise Exception('error format!')
    
    txt.append('magic:%s, h_unk1:%d, h_unk2:%d, inst_cnt:%d, h_unk3:%d, h_tag:%s' % 
               (magic, h_unk1, h_unk2, inst_cnt, h_unk3, h_tag))
    txt.append('')

    for i in range(inst_cnt):
        op, int_cnt, str_cnt, unk = parse_cmd(stm.readu32())
        txt.append('op:%d, int_cnt:%d, str_cnt:%d, unk:%d' % (op, int_cnt, str_cnt, unk))
        line = 'int:'
        ints = []
        for i in range(int_cnt):
            val = stm.readu32()
            line += ' %d,' % val
            ints.append(val)
        txt.append('\t' + line)
        strs = []
        for i in range(str_cnt):
            strs.append(stm.readstr())

        for s in strs:
            decoded_str = decode_with_special(s, cp)
            txt.append('\t' + decoded_str)
            
        if op == 28:
            if ints[0] in name_table:
                pure_txt.append('$' + name_table[ints[0]])
            for s in strs:
                if s != b'*' and s != b'$noname$' and len(s) != 0 and s.count(b',') < 2:
                    pure_txt.append(decode_with_special(s, cp))
        elif op == 21:
            for s in strs:
                if s != b'*' and s != b'$noname$' and len(s) != 0 and s.count(b',') < 2:
                    pure_txt.append(decode_with_special(s, cp))
        elif op == 48:
            pure_txt.append(decode_with_special(strs[0], cp))
        elif op == 191:
            s = strs[0]
            if not is_half(s, cp):
                pure_txt.append(decode_with_special(s, cp))
        elif op == 203:
            s = strs[0]
            if not is_half(s, cp):
                pure_txt.append(decode_with_special(s, cp))
    return txt, pure_txt

def write_txt(name, txt):
    fs = open(name, 'wb')
    ntxt = [l.replace('\n', '#n') for l in txt]
    fs.write('\r\n'.join(ntxt).encode('u16'))
    fs.close()

def ext_rld(fname1, fname2, name_table, cp):
    fs = open(fname1, 'rb')
    stm = bytefile.ByteFile(fs.read())
    fs.close()
    try:
        txt, pure_txt = parse_rld(stm, name_table, cp)
    except Exception as e:
        print(fname1, 'format error:', str(e))
        return
    if len(pure_txt) > 0:
        write_txt(fname2, pure_txt)
        
def ext_all_rld(path1, path2):
    cp = '932'
    charfile = os.path.join(path1, 'defChara.rld')
    fs = open(charfile, 'rb')
    stm = bytefile.ByteFile(fs.read())
    fs.close()
    txt, pure_txt = parse_rld(stm, {}, cp)
    name_table = parse_name_table(pure_txt)
    for f in os.listdir(path1):
        if not f.endswith('.rld'):
            continue
        ext_rld(os.path.join(path1, f),
                os.path.join(path2, f.replace('.rld', '.txt')),
                name_table,
                cp)

ext_all_rld('./rld', './txt')

