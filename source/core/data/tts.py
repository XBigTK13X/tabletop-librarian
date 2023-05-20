from core.settings import config

import os
import glob
import shutil

FORMAT_LOOKUP = {
    'AssetBundles': ['unity3d'],
    'Audio': ['wav','flac','mp3','ogv'],
    'Models': ['obj'],
    'Images': ['bmp','jpg','jpeg','png'],
    'PDF': ['pdf'],
    'Workshop': []
}

def sanitize(file_path):
     return file_path.replace(':','') \
        .replace('/','') \
        .replace('\\','') \
        .replace('-','') \
        .replace('.','') \
        .replace('_','')

def get_local_glob(mod, remote_path):
    local_glob = f'{mod.source.location}/**/{sanitize(remote_path)}*'
    on_disk = glob.glob(local_glob)
    if on_disk and len(on_disk) > 0:
         return on_disk[0]
    return None

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

def backup_mod(archive_source, mod):
    archive_dir = os.path.join(config.ArchiveCreateDir, mod.name)
    if not os.path.isdir(archive_dir):
        os.mkdir(archive_dir)
        os.mkdir(os.path.join(archive_dir, 'Mods'))
    for dir in FORMAT_LOOKUP.keys():
        os.mkdir(os.path.join(archive_dir, 'Mods', dir))
    mod.parse_manifest()
    shutil.copy(mod.path, os.path.join(archive_dir, 'Mods', 'Workshop', mod.file_name))
    asset_count = 0
    for location in mod.asset_locations:
         local_asset = get_local_glob(mod, location)
         if local_asset:
            asset_count += 1
            backup_asset = local_asset.replace(mod.source.location, archive_dir+'/Mods/')
            shutil.copy(local_asset, backup_asset)
    zip_path = archive_dir
    shutil.make_archive(zip_path, 'zip', archive_dir)
    os.rename(zip_path+'.zip', zip_path+'.ttsmod')
    # TODO If number, then use special subdir
    missing =  f' ({asset_count}_{len(mod.asset_locations)})' if asset_count < len(mod.asset_locations) else ''
    destination_path = os.path.join(archive_source.location, mod.name[0].lower(), mod.name + f'{missing}.ttsmod')
    shutil.copyfile(zip_path+'.ttsmod', destination_path)
    os.remove(zip_path+'.ttsmod')
    shutil.rmtree(archive_dir)

def restore_archive(archive, mod_source):
    temp_archive_path = os.path.join(config.ArchiveCreateDir, os.path.basename(archive.path))
    extract_dir = mod_source.location.replace("Mods",'')
    shutil.copyfile(archive.path, temp_archive_path)
    shutil.unpack_archive(temp_archive_path, extract_dir, 'zip')
    os.remove(temp_archive_path)

