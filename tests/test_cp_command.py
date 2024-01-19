
from CP_Automation.utils.cp_helpers import CP_Helper
# can initiate logger object . Redirect all debug files

class TestCPCommand:

    def __init__(self, cp_helper):
        self.cp_helper = cp_helper


    def test_all_files_copied(self, source, destination):
        '''
        Test that all files are copied

        '''
        # Can use os.walk function to traverse all files in nested dir.
        source_files = self.cp_helper.list_nested_dirs(source)[0]
        destination_files = self.cp_helper.list_nested_dirs(destination)[0]
        missing_files = source_files - destination_files
        assert not missing_files, f"Files are not copied: {missing_files}"
        print("All files are copied successfully")

    def test_data_integrity(self, source, destination):
        '''
        Test data integrity
        Steps:
            1. Get all file path (Including nested dirs also) from source
            2. Sort both lists
            3. Compare md5 of source file with destination
            4. If md5 sum is not same then add it into list
            5. Print all files with different md4 sum.
        '''
        files_with_differnt_md5 = []
        source_files_with_path = sorted(self.cp_helper.list_nested_dirs(source)[1])
        destination_files_with_path = sorted(self.cp_helper.list_nested_dirs(destination)[1])
        for src_file, dest_file in zip(source_files_with_path, destination_files_with_path):
            # Can add another step to check for file permissions
            if self.cp_helper.md5sum(src_file) == self.cp_helper.md5sum(dest_file):
                files_with_differnt_md5.append(src_file)
        assert not files_with_differnt_md5, f'Files with different md5 {files_with_differnt_md5}'

    def test_junk_detection(self, source, destination):
        '''
        Test junk detection
        Steps:
            1. Get all file names from source and destination
            2. Compare destination files with source.
            3. Print all junk files
        '''
        source_files = set(self.cp_helper.list_nested_dirs(source)[0])
        destination_files = set(self.cp_helper.list_nested_dirs(destination)[0])
        junk_files = destination_files - source_files
        assert not junk_files, f'Junk files {junk_files}'

    def test_missing_files(self, source, destination):
        '''
        Test missing files.
        '''
        # Can use os.walk function to traverse all files in nested dir.
        source_files = self.cp_helper.list_nested_dirs(source)[0]
        destination_files = self.cp_helper.list_nested_dirs(destination)[0]
        missing_files = source_files - destination_files
        assert not missing_files, f"Missing files : {missing_files}"

def execute_tests(source, destination):

    test_cp = TestCPCommand(cp_helper= CP_Helper())
    # Test ccase 1
    test_cp.test_all_files_copied(source, destination)

    # Test case 2
    test_cp.test_data_integrity(source, destination)

    # Test case 3
    test_cp.test_junk_detection(source, destination)

    # Test case 4
    test_cp.test_missing_files(source, destination)


if __name__ == '__main__':
    source = '/tmp/source_dir'
    destination = '/tmp/dest_dir'
    # Can use argument parser to take runtime values as input.
    # Code to invoke CP command
    #  cp /tmp/source_dir /tmp/dest_dir
    execute_tests(source=source, destination=destination )