# import os
# from configparser import ConfigParser
#
# import configparser
#
#
# class IniFile_Reader_Writer_Operations:
#
#     def __init__(self, ini_filepath):
#         self.filepath = ini_filepath
#         self.config = configparser.ConfigParser()
#         self.config.read(self.filepath)
#
#     # Return list of sections
#     def get_all_sections(self, file_path):
#         self.config = configparser.ConfigParser()
#
#     # Return true if section exist in config file
#     def check_if_key_present_in_file(self, section):
#         return section in self.config
#
#     # Return list of keys in sections
#     def get_all_keys_in_section(self, section):
#         return self.config.options(section)
#
#     # Return key from section
#     def get_value_from_key_in_section(self, section, key):
#         return self.config.get(section, key)
#
#     # Return key from section
#     def get_multiple_values_from_key_in_section(self, section, key):
#         return self.config.get(section, key).split(",")
#
#
# # obj = IniFile_ReaderWriter_Helpers("../../conf.ini")
# #
# # print(obj.get_all_sections())
# # print(obj.check_if_key_present_in_file("LOCATORS"))
# # print(obj.get_all_keys_in_section("LOCATORS"))
# # print(obj.get_value_from_key_in_section("LOCATORS","name__XPATH"))
