import csv
import json
import re


def extract_day(value):
    day_match = re.search(r'([月火水木金土日])', value)
    return day_match.group() if day_match else None


def extract_numeric(value):
    numeric_part = re.search(r'\d+', value)
    return int(numeric_part.group()) if numeric_part else None


def convert_csv_to_json(csv_file_path, output_json_path):
    json_data = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        row: dict
        for row in reader:
            # 授業形態を今まで分割
            styles = [{"style": style.strip()} for style in row['style'].split(',')]

            # エラーハンドリング用
            schedules = []
            days = row['day'].split(',')
            periods = row['period'].split(',')

            for day_period in zip(days, periods):
                day_value = extract_day(day_period[0].strip())
                period_value = extract_numeric(day_period[1].strip()) if day_period[1] else None
                schedules.append({"day": day_value, "period": period_value})

            # 単位数を数字のみ抽出
            credit = extract_numeric(row['credit'])
            is_giga = str(row['is_giga']).strip().lower() == 'true'

            # Create JSON structure
            entry = {
                "sort_id": f"X{row['index']}",
                "subject_name": row['subject_name'],
                "term": row['term'],
                "about": row['about'],
                "method": row['method'],
                "place": row['place'],
                "lang": row['lang'],
                "year": int(row['year']),
                "semester": row['semester'],
                "is_giga": is_giga,
                "url": row['url'],
                "fields": [
                    {
                        "faculty": row['faculty'],
                        "field": row['field'],
                        "credit": credit
                    }
                ],
                "schedules": schedules,
                "staffs": [
                    {
                        "staff_name": row['staff_name']
                    }
                ],
                "styles": styles
            }

            json_data.append(entry)

    with open(output_json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False, indent=2)

    print(f"Conversion completed. JSON data saved to {output_json_path}")


convert_csv_to_json('syllabus_data.csv', 'output.json')
