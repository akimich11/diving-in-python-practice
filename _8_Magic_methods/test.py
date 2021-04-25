from _8_Magic_methods.solution import File
import os.path
path_to_file = 'some_filename'
os.path.exists(path_to_file)

file_obj = File(path_to_file)
os.path.exists(path_to_file)

file_obj.read()

file_obj.write('some text')

file_obj.read()

file_obj.write('other text')

file_obj.read()

file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')

file_obj_2.write('line 2\n')

new_file_obj = file_obj_1 + file_obj_2
isinstance(new_file_obj, File)

print(new_file_obj)

for line in new_file_obj:
    print(ascii(line))