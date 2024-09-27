import csv
import os
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)
        self.total_count = 0

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        self.total_count += 1
        return item

    def close_spider(self, spider):
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        summary_file_name = os.path.join(
            BASE_DIR, 'results', f'status_summary_{current_time}.csv')

        os.makedirs(os.path.dirname(summary_file_name), exist_ok=True)

        with open(
                summary_file_name, mode='w', encoding='utf-8', newline=''
        ) as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])

            for status, count in self.status_count.items():
                writer.writerow([status, count])

            writer.writerow(['Total', self.total_count])
