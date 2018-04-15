import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleService:
    credentials = None
    gc = None
    worksheet = None
    sheet = None

    def init_service(self, json_credentials):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(json_credentials, scope)
        self.gc = gspread.authorize(credentials)

        self.sheet = self.gc.open_by_url(
            'https://docs.google.com/spreadsheets/d/1_BIffVeWlQiTnmX4ZEBemEpoK-hHGxxPpfgNo1FT2Jw/edit#gid=0')
        self.worksheet = self.sheet.get_worksheet(0)

    def set_sheet(self, index):
        self.worksheet = self.sheet.get_worksheet(index)
        return self.worksheet

    def set_a1(self, animal):
        self.worksheet.update_acell('A1', animal)

    def get_row_count(self):
        return self.worksheet.row_count()

    def add_row(self, cells):
        row = self.get_row_count() + 1
        for col, val in cells:
            self.worksheet.update_cell(row, col, val)


google_service = GoogleService()
