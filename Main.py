import RecEx
import СountDim
import RecDB

def main():
	# Подключаем библиотеки Компас API
	Module7, KompasDocument2D = СountDim.plug_kompas()
	# Считываем размеры
	Dimensions = СountDim.dimensions_read(Module7, KompasDocument2D)
	# Вызываем окно для указания пути сохранения excel-файла
	PathXLXS = RecEx.path_window_xlsx()
	# Сохраняем excel-файл
	RecEx.write_book(Dimensions, PathXLXS)
	# Вызываем окно для указания пути сохранения SQLite-файла
	PathDB = RecDB.path_window_DB()
	# Сохраняем Базу данных
	RecDB.db_read(Dimensions, PathDB)


if __name__ == "__main__":
	main()
