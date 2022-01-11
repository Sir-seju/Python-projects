import os 

os.chdir('FOLDER_PATH_HERE')
for f in os.listdir():
    file, f_ext = (os.path.splitext(f))
    title, prefix = (file.split('_'))
    course, part = prefix.split('Part')
    
    title = title.strip()
    course = course.strip()
    part = part.strip().zfill(2)
    
    new_name = f'{part} - {course}: {title}.'
    
    os.rename(f, new_name)
