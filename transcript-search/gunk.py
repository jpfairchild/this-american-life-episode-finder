# # Remove gunk from folder names
# def remove_folder_name_gunk(path_to_folder):

#     # Check if Exists
#     does_exist = os.path.exists(path_to_folder) 
#     print(does_exist)

#     # Return if false 
#     if does_exist == False:
#         return False
    
#     # check for .
#     elif '.' in path_to_folder:
#         updated_path = path_to_folder.replace('.', '-')
#         new_path = os.rename(path_to_folder, updated_path)
#         return new_path

# new_path = remove_folder_name_gunk(path_to_raw_data)

# print(new_path)


#####
# # check if the path exists already
# if os.path.exists(path_to_raw_data + str(episode)) == True:
#     print(str(episode) + ' This episode is downloaded')
#     pass

# elif os.path.exists(path_to_raw_data + str(episode)) == False: