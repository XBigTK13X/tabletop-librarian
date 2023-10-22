from core.settings import config

from core.util import tl_file

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
     name_only = os.path.splitext(file_path)[0]
     return name_only.replace(':','') \
        .replace('/','') \
        .replace('\\','') \
        .replace('-','') \
        .replace('.','') \
        .replace('_','') \
        .replace('?','')

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
                    return tl_file.path(mod.source.location, subdir, sanitize(remote_path)) + '.' + extension

def backup_mod(archive_source, mod):
    archive_dir = tl_file.path(config.ArchiveCreateDir, mod.name)
    if os.path.isdir(archive_dir):
        shutil.rmtree(archive_dir)
    os.mkdir(archive_dir)
    os.mkdir(tl_file.path(archive_dir, 'Mods'))
    for dir in FORMAT_LOOKUP.keys():
        os.mkdir(tl_file.path(archive_dir, 'Mods', dir))
    mod.parse_manifest()
    shutil.copy(mod.path, tl_file.path(archive_dir, 'Mods', 'Workshop', mod.file_name))
    asset_count = 0
    for location in mod.asset_locations:
         # TODO Use sparse lookup instead of glob
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
    destination_path = tl_file.path(archive_source.location, mod.name[0].lower(), mod.name + f'{missing}.ttsmod')
    shutil.copyfile(zip_path+'.ttsmod', destination_path)
    os.remove(zip_path+'.ttsmod')
    shutil.rmtree(archive_dir)

def restore_archive(archive, mod_source):
    # TODO - This for some reason unpacks in the archive location top directory?
    temp_archive_path = tl_file.path(config.ArchiveCreateDir, os.path.basename(archive.path))
    extract_dir = mod_source.location.replace("Mods",'')
    shutil.copyfile(archive.path, temp_archive_path)
    shutil.unpack_archive(temp_archive_path, extract_dir, 'zip')
    os.remove(temp_archive_path)

