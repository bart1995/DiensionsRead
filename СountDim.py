import pythoncom
import os
from win32com.client import Dispatch, gencache
import LDefin2D
import MiscellaneousHelpers as MH
from decouple import config


def plug_kompas():
	kompas6_constants = gencache.EnsureModule(config('key1', default=''), 0, 1, 0).constants
	kompas6_constants_3d = gencache.EnsureModule(config('key2', default=''), 0, 1, 0).constants
	Module5 = gencache.EnsureModule(config('key3', default=''), 0, 1, 0)
	kompas_object = Module5.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(Module5.KompasObject.CLSID, pythoncom.IID_IDispatch))
	Module7 = gencache.EnsureModule(config('key4', default=''), 0, 1, 0)
	application = Module7.IApplication(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(Module7.IApplication.CLSID, pythoncom.IID_IDispatch))
	MH.iApplication  = application
	Documents = application.Documents
	kompas_document = application.ActiveDocument
	kompas_document_2d = Module7.IKompasDocument2D(kompas_document)
	iDocument2D = kompas_object.ActiveDocument2D()
	return Module7, kompas_document_2d

def dimensions_read(Module7, KompasDocument2D):
	View = KompasDocument2D.ViewsAndLayersManager.Views.ActiveView
	ISymbols2DContainer = Module7.ISymbols2DContainer(View)
	DimensionRead = []
	Deviations = {	'Угол':[ISymbols2DContainer.AngleDimensions.AngleDimension, ISymbols2DContainer.AngleDimensions.Count],
			'Радиус дуги':[ISymbols2DContainer.ArcDimensions.ArcDimension, ISymbols2DContainer.ArcDimensions.Count],
			'Диаметр':[ISymbols2DContainer.DiametralDimensions.DiametralDimension, ISymbols2DContainer.DiametralDimensions.Count],
			'Лин. разм.':[ISymbols2DContainer.LineDimensions.LineDimension, ISymbols2DContainer.LineDimensions.Count],
			'Радиус круга':[ISymbols2DContainer.RadialDimensions.RadialDimension, ISymbols2DContainer.RadialDimensions.Count],
			}
	Number = 0
	for DimensionType, Dimension in Deviations.items():
		for i in range(Dimension[1]):
			Number += 1 
			ValObj = Module7.IDimensionText(Dimension[0](i))
			NomVal = ValObj.NominalValue
			MinVal = ValObj.NominalValue + ValObj.LowDeviationValue
			MaxVal = ValObj.NominalValue + ValObj.HighDeviationValue
			DimensionRead.append((	Number, 
						DimensionType,  	
						float("{0:.2f}".format(NomVal)), 
						float("{0:.2f}".format(MinVal)), 
						float("{0:.2f}".format(MaxVal))
						))
	return DimensionRead
