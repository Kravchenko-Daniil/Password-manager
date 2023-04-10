from PySide6 import QtSql, QtWidgets


class Database:
	def __init__(self):
		super(Database, self).__init__()
		self.create_connection()
		
	def create_connection(self):
		db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
		db.setDatabaseName("passwordsBase.db")

		if not db.open():
			QtWidgets.QMessageBox.critical(None, "Cannot open database", "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
			return False

		query = QtSql.QSqlQuery()
		query.exec("CREATE TABLE IF NOT EXISTS Passwords (ID integer primary key AUTOINCREMENT, Service VARCHAR(20), Login VARCHAR(20), Password VARCHAR(40))")

		return True

	def execute_query(self, sql_query, values=None):
		query = QtSql.QSqlQuery()
		query.prepare(sql_query)
		
		if values is not None:
			for value in values:
				query.addBindValue(value)
				
		query.exec()
	
	def add_new_password_query(self, service, login, password):
		sql_query = "INSERT INTO Passwords (Service, Login, Password) VALUES (?, ?, ?)"
		self.execute_query(sql_query, [service, login, password])

	def delete_password_query(self, id):
		sql_query = "DELETE FROM Passwords WHERE ID=?"
		self.execute_query(sql_query, [id])
	
	# def select_row_query(self, search):
	# 	sql_query = "SELECT * FROM  WHERE Service LIKE '%{}%'"
	# 	self.execute_query(sql_query, search)
		
