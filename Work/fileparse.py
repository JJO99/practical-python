import csv


def parse_csv(filename, select=None, types=None, has_header=True):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성한다.
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        if has_header:
            headers = next(rows)  # 헤더를 읽는다.

            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select  # 원하는 헤더만 읽는다.
            else:
                indices = []
        else:
            indices = []

        records = []

        for row in rows:
            if not row:  # 데이터가 없는 행은 건너뛴다.
                continue

            if indices:   # 헤더 선택 여부에 따라
                row = [row[index] for index in indices]

            if types:   # 형변환 여부에 따라
                conv = [func(val) for func, val in zip(types, row)]
            else:
                conv = row   # 형변환 안해도 conv에 집어넣기

            if not has_header:   # 헤더 여부에 따라 _ 없으면 리스트 있으면 딕셔너리
                record = list(conv)
            else:
                record = dict(zip(headers, conv))

            records.append(record)

        return records
