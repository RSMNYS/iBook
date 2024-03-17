import argparse
import os

class AppArgumentsParser:
    
    def arguments_parser(self):
        parser = argparse.ArgumentParser(description="iBook commands parser")
        parser.add_argument('--open-ai-key', help='Your Open AI Key', required=False)
        args = parser.parse_args()

        if args.open_ai_key:
            self.save_api_key(args.open_ai_key)
        else:
            self.load_api_key()

    def save_api_key(self, api_key):
        os.environ['OPENAI_API_KEY'] = api_key

        with open('api_key.cfg', 'w') as config_file:
            config_file.write(api_key)

    def load_api_key(self):
        try:
            with open('api_key.cfg', 'r') as config_file:
                 os.environ['OPENAI_API_KEY'] = config_file.read().strip()
        except:
            print('Key is not available')