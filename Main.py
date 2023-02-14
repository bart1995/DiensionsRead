import RecEx
import СountDim
import RecDB

def main():
	Module7, KompasDocument2D = СountDim.plug_kompas()
	Dimensions = СountDim.dimensions_read(Module7, KompasDocument2D)
	PathXLXS = RecEx.path_window_xlsx()
	RecEx.write_book(Dimensions, PathXLXS)
	PathDB = RecDB.path_window_DB()
	RecDB.db_read(Dimensions, PathDB)


if __name__ == "__main__":
	main()