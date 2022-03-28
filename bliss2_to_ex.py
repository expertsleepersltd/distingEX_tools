import glob, os, math

subtitutions = []

velocity_switches = 3

start = 0
step = math.floor( 0.5 + 128/velocity_switches )
for i in range(velocity_switches):
	end = min( 127, start + step - 1 )
	subtitutions.append( [ '_%d_%d' % (start,end), '_V%d' % (i+1) ] )
	start = end + 1

notes = [ chr(ord('A')+i) for i in range(7) ]
octaves = range(10)

for octave in octaves:
	for note in notes:
		if note not in [ 'E', 'B' ]:
			subtitutions.append( [ "_"+note+"#"+str(octave)+"_"+note+"#"+str(octave), "" ] )
		subtitutions.append( [ "_"+note+str(octave)+"_"+note+str(octave), "" ] )

print( subtitutions )

files = glob.glob( "*.wav" )

for file in files:
	new_name = file
	for s in subtitutions:
		new_name = new_name.replace( s[0], s[1] )
	bits0 = new_name.split( '_' )
	bits1 = bits0[0].split( ' ' )
	new_name = bits1[0] + '_' + '_'.join( bits0[1:] )
	print( file + "\t-> " + new_name )
	os.rename( file, new_name )
