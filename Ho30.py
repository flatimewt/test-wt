#30
from pfac import fac
import time
start=time.clock()

fac.SetUTA(0)
fac.SetAtom('Ho' )
fac.Closed('1s','2s','2p','3s','3p','3d','4s')

fac.Config('4p6 4d2',group='Gnd.0')
fac.Config('4p5 4d3',group='Gnd.1')
fac.Config('4p6 4d1 4f1',group='Gnd.3')
fac.Config('4p5 4d2 4f1',group='Exc.1')
fac.Config('4p4 4d4',group='Exc.2')
fac.Config('4p6 4d0 4f2',group='Exc.3')

fac.ConfigEnergy(0)
fac.OptimizeRadial(['Gnd.0'])
fac.ConfigEnergy(1)

fac.Structure('Ho.lev.b',['Gnd.0','Gnd.1','Gnd.3','Exc.1','Exc.2','Exc.3'])

fac.MemENTable('Ho.lev.b' )
fac.TransitionTable('Ho.tr.b',['Gnd.1'],['Exc.1'],-1)
fac.TransitionTable('Ho.tr.b',['Gnd.1'],['Exc.2'],-1)
fac.TransitionTable('Ho.tr.b',['Gnd.3'],['Exc.3'],-1)

fac.PrintTable('Ho.lev.b','Ho30.lev',1)
fac.PrintTable('Ho.tr.b','Ho30.tr',1)

end=time.clock()
runtime=end-start
print("Total running time: %s seconds"%runtime)






