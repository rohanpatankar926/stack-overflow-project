##### session4

**for running the python script**
`go to github https://hithub.com/rohanpatankar926`
`copy the link which is inside green button cpoy https link`
`goto vs code`
`git clone https://github.com/rohanpatankar926/stack-overflow-project.git`
`cd stack-overflow-project`
`pip install -r requirements.txt`
`python merge_pipeline.py`

**utils.py**<br>
This has 2 function<br>
1.process_posts<br>
to process the semistructured data to tsv format this is used<br>
2.read_yaml<br>
to read the custom yaml file that we have prepared which is used to read all the necessary directory names....<br>

**training_pipeline/stage1_preparedata.py**
This has 1 main function named prepare_data and one input called config_path which is used for giving path of config.yaml<br>
This will process an entire data and store in `artifacts/prepare_data` directory<br>

**config.yaml**<br>
This consists of key and value pairs where all the metadata of directory names are available.<br>

**merge_pipeline.py**<br>
This is the final script where we merge all the particular `training_pipeline` modules and call at once...<br>
