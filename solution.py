from typing import List
import json


class Solution:
    def __init__(self, data_file_path: str, protocol_json_path: str):
        self.data_file_path = data_file_path
        self.protocol_json_path = protocol_json_path

    # Question 1: What is the version name used in the communication session?
    def q1(self) -> str:
        with open(self.data_file_path, 'r') as file:
            first_line = file.readline()
            first_line_parts = first_line.split(',')   
            messageArr = first_line_parts[4].split(' ') 
            ans = []

            for word in messageArr:
                ans.append(self.hex_to_ascii(word))
            return ' '.join(ans)
               
            
    # Question 2: Which protocols have wrong messages frequency in the session compared to their expected frequency based on FPS?
    def q2(self) -> List[str]:
        frqDict = {}
        fpsDict = {164: 36, 84: 18, 48: 9, 1: 1}
        ans = []
        
        with open(self.data_file_path, 'r') as file:
            for line in file:
                line_parts = line.split(',')
                line_parts[2] = frqDict.get(line_parts[2], 0) + 1

        with open(self.protocol_json_path, 'r') as json_file:
            data = json.load(json_file)

        protocols = data.get('protocols', {})

        
        for id, vals in protocols.items():
            if fpsDict[frqDict[id]] != vals.get('Expected FPR', 0):
                ans.append(id)

        return ans

    # Question 3: Which protocols are listed as relevant for the version but are missing in the data file?
    def q3(self) -> List[str]:
        pass

    # Question 4: Which protocols appear in the data file but are not listed as relevant for the version?
    def q4(self) -> List[str]:
        pass

    # Question 5: Which protocols have at least one message in the session with mismatch between the expected size integer and the actual message content size?
    def q5(self) -> List[str]:
        pass

    # Question 6: Which protocols are marked as non dynamic_size in protocol.json, but appear with inconsistent expected message sizes Integer in the data file?
    def q6(self) -> List[str]:
        pass
    
    def hex_to_ascii(hex_string):
        # Convert the hexadecimal string to bytes
        byte_array = bytes.fromhex(hex_string)
        
        # Decode the bytes to an ASCII string
        ascii_string = byte_array.decode('ascii', 'ignore')  # 'ignore' ignores any non-ASCII byte values
        
        return ascii_string

        

    