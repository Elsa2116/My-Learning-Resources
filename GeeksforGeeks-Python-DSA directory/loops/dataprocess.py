def process_data(data):
        results = []
        for item in data:
            try:
                num = float(item)
                if num < 0:
                    print(f"Skipping negative value: {num}")
                    continue  
                results.append(num * 2)
            except ValueError:
                print(f"Invalid data encountered: {item}")
                continue  
        return results

data = ["10", "20", "-5", "abc", "30", "40.5"]
processed = process_data(data)
print(processed) 