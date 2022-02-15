import csv


def parse_csv(filename, select=None, types=None, has_header=None):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성한다.
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        headers = next(rows)   # 헤더를 읽는다.
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select   # 원하는 헤더만 읽는다.
        else:
            indices = []

        records = []

        for row in rows:
            if not row:  # 데이터가 없는 행은 건너뛴다.
                continue

            if indices:
                row = [row[index] for index in indices]

            if types:
                conv = [func(val) for func, val in zip(types, row)]   # 형변환
                record = dict(zip(headers, conv))
            else:
                record = dict(zip(headers, row))

            records.append(record)

        return records
