import csv


def parse_csv(filename):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성한다.
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        headers = next(rows)   # 헤더를 읽는다.
        records = []
        for row in rows:
            if not row:  # 데이터가 없는 행은 건너뛴다.
                continue
            record = dict(zip(headers, row))
            records.append(record)

        return records
