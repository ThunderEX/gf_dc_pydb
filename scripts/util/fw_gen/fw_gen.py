import os
import zlib
import struct


byteorder = '<'  # little endian
Z_COMPRESSED_IMAGE_COUNTER_START = 0x03
zlib_params = dict(level=9, method=zlib.DEFLATED, wbits=-15, memLevel=9, strategy=4)


def loadlayout(cfg_path):
    segments = []
    with open(cfg_path, encoding='latin1') as f:
        bin_cnt = int(f.readline(), 16)
        filler = struct.pack('B', int(f.readline(), 16))

        for i in range(bin_cnt):
            # note that file is in binary mode so need strip '\n' for each line
            structure = f.readline().strip()
            filename = f.readline().strip()
            startaddr = int(f.readline(), 16)
            endaddr = int(f.readline(), 16)
            if structure in ('_FILE',):
                segments.append(
                    {
                        'filename': filename,
                        'startaddr': startaddr,
                        'endaddr': endaddr,
                        'u_code': None,
                        'chksum': None,
                        'counter': None,
                    }
                )
            elif structure in ('_FILE+_PRIMARY+_UNIQUE_CODE+_SUM+_COUNTER',
                                       '_FILE+_SECONDARY+_UNIQUE_CODE+_SUM+_COUNTER'):
                u_code = int(f.readline(), 16)
                counter = int(f.readline(), 16)
                segments.append(
                    {
                        'filename': filename,
                        'startaddr': startaddr,
                        'endaddr': endaddr,
                        'u_code': u_code,
                        'chksum': 0,
                        'counter': counter,
                    }
                )
            else:
                raise ValueError('Unrecognized structure: %s' % structure)
    return filler, segments


def buildone(output_path, filler, segments):
    with open(output_path, 'wb') as f:
        for seg in segments:
            endlenth = sum(struct.calcsize('I') for e in ['u_code', 'chksum', 'counter'] if seg[e] != None)
            content = open(seg['filename'], 'rb').read()
            if seg['chksum'] != None and len(content) % struct.calcsize('I'):
                raise UserWarning('Error reading 4 complete bytes in %s' % seg['filename'])
            compress = zlib.compressobj(**zlib_params)
            if seg['counter'] != None and seg['counter'] >= Z_COMPRESSED_IMAGE_COUNTER_START:
                content = compress.compress(content) + compress.flush()

            content_len = seg['endaddr'] - seg['startaddr'] + 1 - endlenth
            if content_len - len(content) <= 0:
                raise ValueError('Content too long')
            content += filler * (content_len - len(content))

            if seg['chksum'] != None:
                seg['chksum'] = sum(struct.unpack(byteorder + 'I' * (content_len // 4), content))
                seg['chksum'] %= 256 ** struct.calcsize('I')

            f.write(content)
            for e in ['u_code', 'chksum', 'counter']:
                if seg[e] != None:
                    f.write(struct.pack('%sI' % byteorder, seg[e]))


def search_workspace():
    # look for path of cu3x1App_SRC and store in workpath
    curpath = os.path.realpath(__file__)  # path of current script
    workpath = os.path.dirname(curpath)
    target = 'App_SRC'
    # if current script is in sub-folder of App_SRC,
    # for example: C:\dev\59955_DC_V04.01.00\cu3x1App_SRC\Control\FirmwareGenerator
    if target in curpath:
        while target not in os.path.basename(workpath):
            workpath = os.path.dirname(workpath)
    # otherwise, look up parent folders
    # for example:
    # App_SRC is located @ C:\dev\59955_DC_V04.01.00\cu3x1App_SRC
    # App_SRC is located @ C:\dev\59955_DC_V04.01.00\FirmwareGenerator
    else:
        while True:
            app_src = [folder for folder in os.listdir(workpath) if target in folder]
            if app_src:
                workpath = os.path.join(workpath, app_src[-1])
                break
            elif workpath != os.path.dirname(workpath):
                workpath = os.path.dirname(workpath)
            else:
                # worst case, can't find App_SRC, let user input
                workpath = input('input workpath (path of cu3x1App_SRC):')
                break
    return workpath


def run():
    workpath = search_workspace()

    cfgs = []
    for dirpath, dirnames, filenames in os.walk(workpath):
        cfgs.extend([os.path.join(dirpath, filename) for filename in filenames if filename.lower().endswith('.cfg')])

    while True:
        [print('%s:\t%s' % (i, cfg)) for i, cfg in enumerate(cfgs)]
        index = input('Choose a cfg file below to proceed:')
        if index.isdecimal() and 0 <= int(index) < len(cfgs):
            index = int(index)
            break

    os.chdir(os.path.dirname(cfgs[index]))
    with open(cfgs[index]) as cfgfile:
        while True:
            inputfile = cfgfile.readline()
            if not inputfile:  # EOF
                break
            elif not inputfile.strip():  # empty line
                continue
            else:
                inputfile = inputfile.strip()
                print('reading layout from %s' % inputfile)
                filler, segments = loadlayout(inputfile)
                outputfile = cfgfile.readline().strip()
                print('generating %s' % outputfile)
                buildone(outputfile, filler, segments)


if __name__ == '__main__':
    run()
