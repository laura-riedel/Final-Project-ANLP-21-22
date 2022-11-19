import os
import pandas as pd
from collections import defaultdict
from sklearn.preprocessing import MultiLabelBinarizer

class DontPatronizeMe:

	def __init__(self, train_path, test_path):

		self.train_path = train_path
		self.test_path = test_path
		self.train_task2_df = None
		self.test_set_df = None


	def load_task2(self, return_one_hot=True):
		# decide which function to call based on file ending of train data file
		if self.train_path[-3:] == 'csv':
			self.load_task2_csv()
		elif self.train_path[-3:] == 'tsv':
			self.load_task2_tsv(return_one_hot)
			self.train_task2_df['label'] = self.train_task2_df['label'].apply(lambda x: list(x))
		else:
			raise ValueError(f'{self.train_path} needs to be a .tsv or .csv filepath to be loaded correctly.')


	def load_task2_csv(self):
		# simply load previously saved csv
		self.train_task2_df = pd.read_csv(self.train_path, index_col = 0)

	# Taken from Pérez-Almendros et al. (2020), only renamed
	def load_task2_tsv(self, return_one_hot=True):
		# Reads the data for task 2 and present it as paragraphs with binarized labels (a list with seven positions, "activated or not (1 or 0)",
		# depending on wether the category is present in the paragraph).
		# It returns a pandas dataframe with paragraphs and list of binarized labels.
		tag2id = {
				'Unbalanced_power_relations':0,
				'Shallow_solution':1,
				'Presupposition':2,
				'Authority_voice':3,
				'Metaphors':4,
				'Compassion':5,
				'The_poorer_the_merrier':6
				}
		print('Map of label to numerical label:')
		print(tag2id)
		data = defaultdict(list)
		with open(self.train_path) as f:
			for line in f.readlines()[4:]:
				par_id=line.strip().split('\t')[0]
				art_id = line.strip().split('\t')[1]
				text=line.split('\t')[2]#.lower()
				keyword=line.split('\t')[3]
				country=line.split('\t')[4]
				start=line.split('\t')[5]
				finish=line.split('\t')[6]
				text_span=line.split('\t')[7]
				label=line.strip().split('\t')[-2]
				num_annotators=line.strip().split('\t')[-1]
				labelid = tag2id[label]
				if not labelid in data[(par_id, art_id, text, keyword, country)]:
					data[(par_id,art_id, text, keyword, country)].append(labelid)

		par_ids=[]
		art_ids=[]
		pars=[]
		keywords=[]
		countries=[]
		labels=[]

		for par_id, art_id, par, kw, co in data.keys():
			par_ids.append(par_id)
			art_ids.append(art_id)
			pars.append(par)
			keywords.append(kw)
			countries.append(co)

		for label in data.values():
			labels.append(label)

		if return_one_hot:
			labels = MultiLabelBinarizer().fit_transform(labels)
		df = pd.DataFrame(list(zip(par_ids, 
									art_ids, 
									pars, 
									keywords,
									countries, 
									labels)), columns=['par_id',
														'art_id', 
														'text', 
														'keyword',
														'country', 
														'label',
														])
		self.train_task2_df = df



	def load_test(self):
		# decide which function to call based on file ending of test data file
		if self.test_path[-3:] == 'csv':
			self.load_test_csv()
		elif self.test_path[-3:] == 'tsv':
			self.load_test_tsv()
		else:
			raise ValueError(f'{self.test_path} needs to be a .tsv or .csv filepath to be loaded correctly.')


	# Taken from Pérez-Almendros et al. (2020), only renamed and label column in dataframe added
	def load_test_tsv(self):
		rows=[]
		with open(self.test_path) as f:
			for line in f:
				t=line.strip().split('\t')
				rows.append(t)
		self.test_set_df = pd.DataFrame(rows, columns="par_id art_id text keyword country label".split())


	def load_test_csv(self):
		# simply load previously saved csv
		self.test_set_df = pd.read_csv(self.test_path, index_col = 0)
		