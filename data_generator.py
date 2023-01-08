import json
import numpy as np


class DataGenerator(object):

    def __init__(self, dimension, records, init_domain_id):
        self.dimension = dimension
        self.records = records
        self.init_domain_id = init_domain_id

    def np_encoder(object):
        if isinstance(object, np.generic):
            return object.item()

    def run(self):
        with open('/Users/xiyaoli/Desktop/Study/research_program/'
                  'information_element/i_tree_data/data/initDomains/initDomains.json') as f:
            init_domains = json.load(f)

        init_domain = list(filter(lambda x: x.get('id') == self.init_domain_id, init_domains['data']))[0]
        print(init_domain)

        record_id = 1
        records = []

        coefficient_prefix = 'coefficient_x'
        # records_template = {
        #     'constant': 0
        # }

        random_coefficients = list(np.random.randint(0, 1000, size=self.records * self.dimension))
        # random_constants = list(np.random.randint(0, size=self.records))
        random_constants = [0] * self.records
        for i in range(0, len(random_coefficients), self.dimension):
            record_template = {
                'constant': 0
            }
            counter = 1
            record_template['id'] = record_id
            for j in range(self.dimension):
                coefficient = coefficient_prefix + str(counter)
                record_template[coefficient] = int(random_coefficients[i+j])
                record_template['constant'] = int(random_constants[int(i / self.dimension)])
                counter = counter + 1
            records.append(record_template)
            print(records)
            record_id = record_id + 1

        print(records)
        filename = 'data_d_' + str(self.dimension) + '_records_' +\
                   str(self.records) + '_initDomainID_' + str(self.init_domain_id) + '.json'

        with open('/Users/xiyaoli/Desktop/Study/research_program/'
                  'information_element/i_tree_data/data/input/' + filename, 'w') as f:
            f.write(json.dumps({'records': records}))
