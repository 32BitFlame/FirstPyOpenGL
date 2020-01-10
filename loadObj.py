def dump(fileName):
	"""Returns the Dump data from an obj file as a tuple formated like (vertices, edges, surfaces, obj_name)"""
	vertices = []
	edges = []
	faces = []
	obj_name = ""
	with open(fileName, "r") as f:
		line = ""
		i = 0
		for line in f:
			try:
				line = f.readline()
				if(line.startswith("#") or line.startswith("mtllib")):
					continue
				txt = line[2:(len(line) - 1)]
				if(line.startswith("o")):
					#Dump object name
					obj_name = txt
				if(line.startswith("vt")):
					continue
				if(line.startswith("v")):
					#Add verti
					verts = txt.split()
					for i in range(len(verts)):
						verts[i] = float(verts[i])
					vertices.append(tuple(verts))
					print(verts)
				if(line.startswith("f")):
					_txt = txt.split()
					points = []
					for t in _txt:
						__txt = t.split("/")
						points.append(int(__txt[0]))
					faces.append(tuple(points))
					
			except(EOFError):
				break
			except:
				break
			finally:
				i += 1
	return_tuple = (tuple(vertices), tuple(edges), tuple(faces), obj_name)
	print("Model Dumps: '{name}' {0} Vertices, {1} Edges, {2} faces".format(len(vertices), len(edges), len(faces), name = obj_name))
	return return_tuple

if(__name__ == "__main__"):
	print("main")
	dat = dump("untitled.obj")
	print(dat[0][0:12])
	print(dat[2][5])
