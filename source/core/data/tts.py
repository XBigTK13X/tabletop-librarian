import os
import glob

FORMAT_LOOKUP = {
    'AssetBundles': ['unity3d'],
    'Models': ['obj'],
    'Audio': ['wav','flac','mp3','ogv'],
    'Images': ['bmp','jpg','jpeg','png'],
    'PDF': ['pdf']
}

def sanitize(file_path):
     return file_path.replace(':','') \
        .replace('/','') \
        .replace('\\','') \
        .replace('-','') \
        .replace('.','') \
        .replace('_','')

def local_file_exists(mod, remote_path):
    on_disk = glob.glob(f'{mod.source.location}/**{sanitize(remote_path)}*')
    return on_disk and len(on_disk) > 0

def get_local_path(mod, remote_path, extension):
        extension_search = extension.lower()
        for subdir, formats in FORMAT_LOOKUP.items():
            for format in formats:
                if format == extension_search:
                    sanitized = remote_path \
                        .replace(':','') \
                        .replace('/','') \
                        .replace('\\','') \
                        .replace('-','') \
                        .replace('.','') \
                        .replace('_','')
                    return os.path.join(mod.source.location, subdir, sanitized) + '.' + extension