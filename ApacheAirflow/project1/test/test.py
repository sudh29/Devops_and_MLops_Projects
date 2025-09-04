import unittest
from datetime import datetime
from airflow.utils.context import Context
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.first_airflow import ExtractOperator, TransformOperator, LoadOperator

class TestETLOperators(unittest.TestCase):
    def setUp(self):
        self.context = Context({
            'task_instance': None,
            'execution_date': datetime.now()
        })

    def test_extract_operator(self):
        extract = ExtractOperator(
            task_id='test_extract',
            source_system='test_source'
        )
        result = extract.process(self.context)
        self.assertEqual(result['source'], 'test_source')
        self.assertEqual(result['data'], 'sample_data')

    def test_transform_operator(self):
        transform = TransformOperator(
            task_id='test_transform',
            transformation_type='test_transformation'
        )
        # Mock the context with input data
        self.context['task_instance'] = type('obj', (object,), {
            'xcom_pull': lambda task_ids: {'source': 'test', 'data': 'test_data'}
        })
        self.context['task'] = type('obj', (object,), {'upstream_task_ids': {'test_extract'}})
        
        result = transform.process(self.context)
        self.assertTrue(result['transformed'])

    def test_load_operator(self):
        load = LoadOperator(
            task_id='test_load',
            target_system='test_target'
        )
        # Mock the context with input data
        self.context['task_instance'] = type('obj', (object,), {
            'xcom_pull': lambda task_ids: {'source': 'test', 'data': 'test_data', 'transformed': True}
        })
        self.context['task'] = type('obj', (object,), {'upstream_task_ids': {'test_transform'}})
        
        # Should not raise any exceptions
        load.process(self.context)

if __name__ == '__main__':
    unittest.main()