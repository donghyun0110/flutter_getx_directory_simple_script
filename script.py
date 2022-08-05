import subprocess
import os
import sys

path = sys.argv[1]
file_name = sys.argv[2]

os.chdir(path)
os.mkdir(file_name)
os.chdir(file_name)
with open(f'{file_name}_binding.dart', 'w') as f:
    f.write(f"import 'package:fit_seoul/modules/{file_name}/{file_name}_controller.dart';\n")
    f.write("import 'package:get/get.dart';\n")
    f.write(f"class {file_name.capitalize()}binding extends GetxController {{\n")
    f.write("@override\n")
    f.write("List<Bind> dependencies() {\n")
    f.write("return [\n")
    f.write(f"Bind.lazyPut<{file_name.capitalize()}Controller>(\n")
    f.write(f"() => {file_name.capitalize()}Controller(),\n")
    f.write(")")
    f.write("];\n")
    f.write("}\n")
    f.write("}\n")


with open(f'{file_name}_controller.dart', 'w') as f:
    f.write("import 'package:get/get.dart';\n")
    f.write(f"class {file_name.capitalize()}Controller extends GetxController {{}}\n")

with open(f'{file_name}_view.dart', 'w') as f:
    f.write(f"import 'package:fit_seoul/modules/{file_name}/{file_name}_controller.dart';\n")
    f.write("import 'package:flutter/material.dart';\n")
    f.write("import 'package:get/get.dart';\n")
    f.write(f"class {file_name.capitalize()}View extends GetView<{file_name.capitalize()}Controller> {{\n")
    f.write("@override\n")
    f.write("Widget build(BuildContext context) {\nreturn Scaffold();\n}\n}\n")
