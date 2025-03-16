#!/bin/python3

class Table:
    def __init__(self, fields=None, title=None, rows=[]):
        self.fileds = fields
        self.title = title
        self.rows = rows
        self.showRows = []
        self.clomnMax = [0] * len(fields)
        self.lengthMax = sum(self.clomnMax)
        # \033 is esc, 35 is Magenta color, 1 is Bold
        self.frmFmt = "\033[1;35m"
        self.txtFmt = "\033[1;36m"
        self.fmtEnd = "\033[0m"
        self.frmStr = "╔╦╗╠╬╣╚╩╝ ═══║║║"
        self.frmNam = ('topL','topM','topR','midL','midM','midR','btmL','btmM','btmR',\
                      'txtEpt','topRow','midRow','btmRow','lftCol','midCol','ritCol')
        self.frmSym = [self.fmt(x) for x in self.frmStr]
        self.frame  = dict(zip(self.frmNam, self.frmSym))
    
    def fmt(self, s, fmtCode='frm'):
        if fmtCode == 'frm':
            return self.frmFmt + s + self.fmtEnd
        elif fmtCode == 'txt':
            return self.txtFmt + s + self.fmtEnd
        else:
            return s

    def add_row(self, row):
        self.rows.append(row)

    def gen_frame(self, position):
        frame = self.frame
        if position == 'titleTop':
            s = frame['topL'] + frame['topRow'] * self.lengthMax + frame['topR']
        elif position == 'titleBtmMid':
            m = frame['topM'].join([frame['midRow'] * l for l in self.clomnMax])
            s = frame['midL'] + m + frame['midR']
        elif position == 'titleTopMid':
            m = frame['btmM'].join([frame['midRow'] * l for l in self.clomnMax])
            s = frame['midL'] + m + frame['midR']
        elif position == 'titleBtm':
            s = frame['btmL'] + frame['btmRow'] * self.lengthMax + frame['btmR']
        elif position == 'top':
            m = frame['topM'].join([frame['topRow'] * l for l in self.clomnMax])
            s = frame['topL'] + m + frame['topR']
        elif position == 'mid':
            m = frame['midM'].join([frame['midRow'] * l for l in self.clomnMax])
            s = frame['midL'] + m + frame['midR']
        elif position == 'btm':
            m = frame['btmM'].join([frame['btmRow'] * l for l in self.clomnMax])
            s = frame['btmL'] + m + frame['btmR']
        return s

    def gen_row(self, row, title=False):
        frame = self.frame
        clMax = self.clomnMax
        ept = frame['txtEpt']
        if title == True:
            if len(row) < self.lengthMax:
                s = frame['lftCol'] + ept * ((self.lengthMax - len(row)) // 2) + row + \
                        ept * ((self.lengthMax - len(row) + 1) // 2) + frame['ritCol']
            else:
                s = '' 
        else:
            rowpad = [ept + str(row[i]) + ept * (clMax[i] - len(str(row[i])) - 1) for i in range(len(row))]
            m = frame['midCol'].join([c for c in rowpad])
            s = frame['lftCol'] + m + frame['ritCol']
        return s

    def preprocess_table(self):
        self.clomnMax = [max(len(str(item)) + 2 for item in col) for col in zip(*self.rows)]
        self.lengthMax = sum(self.clomnMax) + (len(self.clomnMax) - 1)

    def show(self):
        self.preprocess_table()
        if self.title is not None:
            self.showRows.append(self.gen_frame('titleTop'))
            self.showRows.append(self.gen_row(self.title, title=True))
            self.showRows.append(self.gen_frame('titleBtmMid'))
        else:
            self.showRows.append(self.gen_frame('top'))
        for row in self.rows[:-1]:
            self.showRows.append(self.gen_row(row))
            self.showRows.append(self.gen_frame('mid'))
        self.showRows.append(self.gen_row(self.rows[-1]))
        self.showRows.append(self.gen_frame('btm'))
        s = '\n'.join(self.showRows)
        print(s)

if __name__ == '__main__':
    tab = Table(['Address', 'Bytes3', 'Bytes2', 'Bytes1', 'Bytes0'])
    tab.title = "https://www.cnblogs.com/TOMOCAT/p/13041112.html"
    tab.add_row([0, '', 'pid: 9999', '9999999999999', 'vid: 4020'])
    tab.add_row([0, None, None, '', 'vid: 4030'])
    tab.add_row([0x03, '', None, '', 'vid: 4050'])

    tab.show()
