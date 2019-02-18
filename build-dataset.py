import zipfile, random, os


TRAIN_PATH= "train"
TEST_PATH= "test"

# Function unzips the
def build_dataset( data_file ):

    dandelion = []
    daisy = []
    rose = []
    sunflower = []
    tulip = []
    zip_file = zipfile.ZipFile( data_file )
    for file_name in zip_file.namelist():
        if "daisy" in file_name:
            if "daisy/" != file_name:
                daisy.append( file_name )
        elif "dandelion" in file_name:
            if "dandelion/" != file_name:
                dandelion.append( file_name )
        elif "rose" in file_name:
            if "rose/" != file_name:
                rose.append( file_name )
        elif "sunflower" in file_name:
            if "sunflower/" != file_name:
                sunflower.append( file_name )
        elif "tulip" in file_name:
            if "tulip/" != file_name:
                tulip.append( file_name )
    dict = {}
    dict["daisy"] = daisy
    dict["dandelion"] = dandelion
    dict["rose"] = rose
    dict["sunflower"] = sunflower
    dict["tulip"] = tulip

    for label in dict:
        # Randomize the list of images for randomized data
        random.shuffle( dict[label] )
        # 80% train, 20% test split
        train_len = int(.8*len(dict[label]))
        i = 0
        while i < train_len:
            zip_file.extract( dict[label][i], os.path.join("", "train"))
            i += 1
        while i < len(dict[label]):
            zip_file.extract( dict[label][i], os.path.join("", "test"))
            i += 1

# Function checks if the test and train directories exist, if they do delete
# those directories and its contents, then recreate the test and train directory
# again
def setup_workspace( path ):

    # If test or train path already exists go delete the test or train directory
    # and all the contents inside the directory
    # Assumptions made:
    # 1. After the train or test folder there are 5 subfolders of the labels
    # 2. Inside each subfolder are regular files ( images in the case for this
    #     project )
    if os.path.exists(path):
        subfolders = os.listdir(path)
        # Subfolder directories
        for subfolder in subfolders:
            subfolder_name = os.path.join(path, subfolder)
            files = os.listdir( subfolder_name )
            # For files in the subfolder
            for file in files:
                os.remove(os.path.join(subfolder_name, file))
            os.removedirs(subfolder_name)
    os.mkdir(path)

###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':

    # setup workspace in train and test path
    setup_workspace(TRAIN_PATH)
    setup_workspace(TEST_PATH)
    build_dataset( "flowers.zip" )