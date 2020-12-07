import Metashape as mt

# VARIABLES
chunk = mt.app.document.chunk #define active chunk
markers = chunk.markers #define present markers
total_targets = 0 #intitial condition

#ref_file = mt.app.getOpenFileName("Choose reference coordinate file")

# Loop that cicles every marker present and counts the respective projections
for marker in markers:
	total_targets += len(marker.projections)

print("Total detected targets: {}".format(len(markers)))

if total_targets == 135:
	print("Total number of target projections: {}".format(total_targets))
	print("The number of expected GCPs has been detected. You can continue with the next round.")

else:
	print("NOTE: The number of GCPs detected is different from 135")

#chunk.importReference(path=ref_file, format=Metashape.ReferenceFormatCSV, columns='nxyz', delimiter=';')
