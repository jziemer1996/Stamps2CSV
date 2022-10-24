import csv
import os

### Columns ###
## Analysis-ready RStudio CSV format ##


def columns(working_dir, output_dir, stamps_csv, output_csv):
    with open(working_dir + stamps_csv, 'r') as file:
        reader = csv.reader(file)
        n = 1
        with open(output_dir + output_csv, 'w',
                  newline='') as f:
            # You need to add every single deformation value of an PS as a new list element
            # example header = ['ID', 'Lat', 'Lon', 'Trend (mm/y)', 'Deformation X in mm at date yyyymmdd']
            header = ['ID', 'Lat', 'Lon', 'Coh', 'Var', 'Trend', 'Def_1', 'Def_2', 'Def_3', 'Def_4', 'Def_5', 'Def_6',
                      'Def_7', 'Def_8', 'Def_9', 'Def_10', 'Def_11', 'Def_12', 'Def_13', 'Def_14', 'Def_15', 'Def_16',
                      'Def_17', 'Def_18', 'Def_19', 'Def_20', 'Def_21', 'Def_22', 'Def_23','Def_24', 'Def_25', 'Def_26',
                      'Def_27', 'Def_28', 'Def_29', 'Def_30', 'Def_31', 'Def_32', 'Def_33', 'Def_34', 'Def_35', 'Def_36',
                      'Def_37', 'Def_38', 'Def_39', 'Def_40', 'Def_41', 'Def_42', 'Def_43', 'Def_44', 'Def_45', 'Def_46',
                      'Def_47', 'Def_48', 'Def_49', 'Def_50', 'Def_51', 'Def_52', 'Def_53', 'Def_54', 'Def_55', 'Def_56',
                      'Def_57', 'Def_58', 'Def_59', 'Def_60', 'Def_61', 'Def_62', 'Def_63', 'Def_64', 'Def_65', 'Def_66',
                      'Def_67', 'Def_68', 'Def_69','Def_70', 'Def_71', 'Def_72', 'Def_73', 'Def_74', 'Def_75', 'Def_76',
                      'Def_77', 'Def_78', 'Def_79', 'Def_80', 'Def_81', 'Def_82', 'Def_83', 'Def_84', 'Def_85', 'Def_86',
                      'Def_87', 'Def_88', 'Def_89', 'Def_90', 'Def_91', 'Def_92','Def_93', 'Def_94', 'Def_95', 'Def_96',
                      'Def_97', 'Def_98', 'Def_99', 'Def_100', 'Def_101', 'Def_102', 'Def_103', 'Def_104', 'Def_105',
                      'Def_106', 'Def_107', 'Def_108', 'Def_109', 'Def_110', 'Def_111', 'Def_112', 'Def_113', 'Def_114',
                      'Def_115','Def_116', 'Def_117', 'Def_118', 'Def_119', 'Def_120', 'Def_121', 'Def_122', 'Def_123',
                      'Def_124', 'Def_125', 'Def_126', 'Def_127', 'Def_128', 'Def_129', 'Def_130', 'Def_131', 'Def_132',
                      'Def_133', 'Def_134', 'Def_135', 'Def_136', 'Def_137', 'Def_138','Def_139', 'Def_140', 'Def_141',
                      'Def_142', 'Def_143', 'Def_144', 'Def_145', 'Def_146', 'Def_147', 'Def_148', 'Def_149', 'Def_150',
                      'Def_151', 'Def_152', 'Def_153', 'Def_154', 'Def_155', 'Def_156', 'Def_157', 'Def_158', 'Def_159',
                      'Def_160', 'Def_161','Def_162', 'Def_163', 'Def_164', 'Def_165', 'Def_166', 'Def_167', 'Def_168',
                      'Def_169', 'Def_170', 'Def_171', 'Def_172', 'Def_173', 'Def_174', 'Def_175', 'Def_176', 'Def_177',
                      'Def_178', 'Def_179', 'Def_180', 'Def_181', 'Def_182', 'Def_183', 'Def_184','Def_185', 'Def_186',
                      'Def_187', 'Def_188', 'Def_189', 'Def_190', 'Def_191', 'Def_192', 'Def_193', 'Def_194', 'Def_195',
                      'Def_196', 'Def_197', 'Def_198', 'Def_199', 'Def_200', 'Def_201', 'Def_202', 'Def_203', 'Def_204',
                      'Def_205', 'Def_206', 'Def_207','Def_208', 'Def_209', 'Def_210', 'Def_211', 'Def_212', 'Def_213',
                      'Def_214', 'Def_215', 'Def_216', 'Def_217','Def_218','Def_219', 'Def_220', 'Def_221', 'Def_222',
                      'Def_223', 'Def_224', 'Def_225', 'Def_226', 'Def_227']
            writer = csv.writer(f)
            writer.writerow(header)
            # Create multiple empty lists
            list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10, list_11, list_12, \
            list_13, list_14, list_15, list_16, list_17, list_18, list_19, list_20, list_21, list_22, list_23, list_24, \
            list_25, list_26, list_27, list_28, list_29, list_30, list_31, list_32, list_33, list_34, list_35, list_36, \
            list_37, list_38, list_39, list_40, list_41, list_42, list_43, list_44, list_45, list_46, list_47, list_48, \
            list_49, list_50, list_51, list_52, list_53, list_54, list_55, list_56, list_57, list_58, list_59, list_60, \
            list_61, list_62, list_63, list_64, list_65, list_66, list_67, list_68, list_69, list_70, list_71, list_72, \
            list_73, list_74, list_75, list_76, list_77, list_78, list_79, list_80, list_81, list_82, list_83, list_84, \
            list_85, list_86, list_87, list_88, list_89, list_90, list_91, list_92, list_93, list_94, list_95, list_96, \
            list_97, list_98, list_99, list_100, list_101, list_102, list_103, list_104, list_105, list_106, list_107, \
            list_108, list_109, list_110, list_111, list_112, list_113, list_114, list_115, list_116, list_117, list_118, \
            list_119, list_120, list_121, list_122, list_123, list_124, list_125, list_126, list_127, list_128, list_129, \
            list_130, list_131, list_132, list_133, list_134, list_135, list_136, list_137, list_138, list_139, list_140, \
            list_141, list_142, list_143, list_144, list_145, list_146, list_147, list_148, list_149, list_150, list_151, \
            list_152, list_153, list_154, list_155, list_156, list_157, list_158, list_159, list_160, list_161, list_162, \
            list_163, list_164, list_165, list_166, list_167, list_168, list_169, list_170, list_171, list_172, list_173, \
            list_174, list_175, list_176, list_177, list_178, list_179, list_180, list_181, list_182, list_183, list_184, \
            list_185, list_186, list_187, list_188, list_189, list_190, list_191, list_192, list_193, list_194, list_195, \
            list_196, list_197, list_198, list_199, list_200, list_201, list_202, list_203, list_204, list_205, list_206, \
            list_207, list_208, list_209, list_210, list_211, list_212, list_213, list_214, list_215, list_216, list_217, \
            list_218, list_219, list_220, list_221, list_222, list_223, list_224, list_225, list_226, list_227, list_228, \
            list_229, list_230, list_231, list_232 = ([] for i in range(233))

            id = -2  # Point ID starts at "1", because first two rows of the STAMPS Visualizer output CSV are not useful!
            for row in reader:
                id += 1
                # If you add deformation values above, you need to append the values to a new list
                list_0.append(id), list_1.append(row[0]), list_2.append(row[1]), list_3.append(row[2]), \
                list_4.append(row[3]), list_5.append(row[4]), list_6.append(row[5]), list_7.append(row[6]), \
                list_8.append(row[7]), list_9.append(row[8]), list_10.append(row[9]), list_11.append(row[10]), \
                list_12.append(row[11]), list_13.append(row[12]), list_14.append(row[13]), list_15.append(row[14]), \
                list_16.append(row[15]), list_17.append(row[16]), list_18.append(row[17]), list_19.append(row[18]), \
                list_20.append(row[19]), list_21.append(row[20]), list_22.append(row[21]), list_23.append(row[22]), \
                list_24.append(row[23]), list_25.append(row[24]), list_26.append(row[25]), list_27.append(row[26]),
                list_28.append(row[27]), list_29.append(row[28]), list_30.append(row[29]), list_31.append(row[30]),
                list_32.append(row[31]), list_33.append(row[32]), list_34.append(row[33]), list_35.append(row[34]),
                list_36.append(row[35]), list_37.append(row[36]), list_38.append(row[37]), list_39.append(row[38]),
                list_40.append(row[39]), list_41.append(row[40]), list_42.append(row[41]), list_43.append(row[42]),
                list_44.append(row[43]), list_45.append(row[44]), list_46.append(row[45]), list_47.append(row[46]),
                list_48.append(row[47]), list_49.append(row[48]), list_50.append(row[49]), list_51.append(row[50]),
                list_52.append(row[51]), list_53.append(row[52]), list_54.append(row[53]), list_55.append(row[54]),
                list_56.append(row[55]), list_57.append(row[56]), list_58.append(row[57]), list_59.append(row[58]),
                list_60.append(row[59]), list_61.append(row[60]), list_62.append(row[61]), list_63.append(row[62]),
                list_64.append(row[63]), list_65.append(row[64]), list_66.append(row[65]), list_67.append(row[66]),
                list_68.append(row[67]), list_69.append(row[68]), list_70.append(row[69]), list_71.append(row[70]),
                list_72.append(row[71]), list_73.append(row[72]), list_74.append(row[73]), list_75.append(row[74]),
                list_76.append(row[75]), list_77.append(row[76]), list_78.append(row[77]), list_79.append(row[78]),
                list_80.append(row[79]), list_81.append(row[80]), list_82.append(row[81]), list_83.append(row[82]),
                list_84.append(row[83]), list_85.append(row[84]), list_86.append(row[85]), list_87.append(row[86]),
                list_88.append(row[87]), list_89.append(row[88]), list_90.append(row[89]), list_91.append(row[90]),
                list_92.append(row[91]), list_93.append(row[92]), list_94.append(row[93]), list_95.append(row[94]),
                list_96.append(row[95]), list_97.append(row[96]), list_98.append(row[97]), list_99.append(row[98]),
                list_100.append(row[99]), list_101.append(row[100]), list_102.append(row[101]), list_103.append(row[102]),
                list_104.append(row[103]), list_105.append(row[104]), list_106.append(row[105]), list_107.append(row[106]),
                list_108.append(row[107]), list_109.append(row[108]), list_110.append(row[109]), list_111.append(row[110]),
                list_112.append(row[111]), list_113.append(row[112]), list_114.append(row[113]), list_115.append(row[114]),
                list_116.append(row[115]), list_117.append(row[116]), list_118.append(row[117]), list_119.append(row[118]),
                list_120.append(row[119]), list_121.append(row[120]), list_122.append(row[121]), list_123.append(row[122]),
                list_124.append(row[123]), list_125.append(row[124]), list_126.append(row[125]), list_127.append(row[126]),
                list_128.append(row[127]), list_129.append(row[128]), list_130.append(row[129]), list_131.append(row[130]),
                list_132.append(row[131]), list_133.append(row[132]), list_134.append(row[133]), list_135.append(row[134]),
                list_136.append(row[135]), list_137.append(row[136]), list_138.append(row[137]), list_139.append(row[138]),
                list_140.append(row[139]), list_141.append(row[140]), list_142.append(row[141]), list_143.append(row[142]),
                list_144.append(row[143]), list_145.append(row[144]), list_146.append(row[145]), list_147.append(row[146]),
                list_148.append(row[147]), list_149.append(row[148]), list_150.append(row[149]), list_151.append(row[150]),
                list_152.append(row[151]), list_153.append(row[152]), list_154.append(row[153]), list_155.append(row[154]),
                list_156.append(row[155]), list_157.append(row[156]), list_158.append(row[157]), list_159.append(row[158]),
                list_160.append(row[159]), list_161.append(row[160]), list_162.append(row[161]), list_163.append(row[162]),
                list_164.append(row[163]), list_165.append(row[164]), list_166.append(row[165]), list_167.append(row[166]),
                list_168.append(row[167]), list_169.append(row[168]), list_170.append(row[169]), list_171.append(row[170]),
                list_172.append(row[171]), list_173.append(row[172]), list_174.append(row[173]), list_175.append(row[174]),
                list_176.append(row[175]), list_177.append(row[176]), list_178.append(row[177]), list_179.append(row[178]),
                list_180.append(row[179]), list_181.append(row[180]), list_182.append(row[181]), list_183.append(row[182]),
                list_184.append(row[183]), list_185.append(row[184]), list_186.append(row[185]), list_187.append(row[186]),
                list_188.append(row[187]), list_189.append(row[188]), list_190.append(row[189]), list_191.append(row[190]),
                list_192.append(row[191]), list_193.append(row[192]), list_194.append(row[193]), list_195.append(row[194]),
                list_196.append(row[195]), list_197.append(row[196]), list_198.append(row[197]), list_199.append(row[198]),
                list_200.append(row[199]), list_201.append(row[200]), list_202.append(row[201]), list_203.append(row[202]),
                list_204.append(row[203]), list_205.append(row[204]), list_206.append(row[205]), list_207.append(row[206]),
                list_208.append(row[207]), list_209.append(row[208]), list_210.append(row[209]), list_211.append(row[210]),
                list_212.append(row[211]), list_213.append(row[212]), list_214.append(row[213]), list_215.append(row[214]),
                list_216.append(row[215]), list_217.append(row[216]), list_218.append(row[217]), list_219.append(row[218]),
                list_220.append(row[219]), list_221.append(row[220]), list_222.append(row[221]), list_223.append(row[222]),
                list_224.append(row[223]), list_225.append(row[224]), list_226.append(row[225]), list_227.append(row[226]),
                list_228.append(row[227]), list_229.append(row[228]), list_230.append(row[229]), list_231.append(row[230]),
                list_232.append(row[231])
                rows = zip(list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10,
                           list_11, list_12, list_13, list_14, list_15, list_16, list_17, list_18, list_19, list_20,
                           list_21, list_22, list_23, list_24, list_25, list_26, list_27, list_28, list_29, list_30,
                           list_31, list_32, list_33, list_34, list_35, list_36, list_37, list_38, list_39, list_40,
                           list_41, list_42, list_43, list_44, list_45, list_46, list_47, list_48, list_49, list_50,
                           list_51, list_52, list_53, list_54, list_55, list_56, list_57, list_58, list_59, list_60,
                           list_61, list_62, list_63, list_64, list_65, list_66, list_67, list_68, list_69, list_70,
                           list_71, list_72, list_73, list_74, list_75, list_76, list_77, list_78, list_79, list_80,
                           list_81, list_82, list_83, list_84, list_85, list_86, list_87, list_88, list_89, list_90,
                           list_91, list_92, list_93, list_94, list_95, list_96, list_97, list_98, list_99, list_100,
                           list_101, list_102, list_103, list_104, list_105, list_106, list_107, list_108, list_109,
                           list_110, list_111, list_112, list_113, list_114, list_115, list_116, list_117, list_118,
                           list_119, list_120, list_121, list_122, list_123, list_124, list_125, list_126, list_127,
                           list_128, list_129, list_130, list_131, list_132, list_133, list_134, list_135, list_136,
                           list_137, list_138, list_139, list_140, list_141, list_142, list_143, list_144, list_145,
                           list_146, list_147, list_148, list_149, list_150, list_151, list_152, list_153, list_154,
                           list_155, list_156, list_157, list_158, list_159, list_160, list_161, list_162, list_163,
                           list_164, list_165, list_166, list_167, list_168, list_169, list_170, list_171, list_172,
                           list_173, list_174, list_175, list_176, list_177, list_178, list_179, list_180, list_181,
                           list_182, list_183, list_184, list_185, list_186, list_187, list_188, list_189, list_190,
                           list_191, list_192, list_193, list_194, list_195, list_196, list_197, list_198, list_199,
                           list_200, list_201, list_202, list_203, list_204, list_205, list_206, list_207, list_208,
                           list_209, list_210, list_211, list_212, list_213, list_214, list_215, list_216, list_217,
                           list_218, list_219, list_220, list_221, list_222, list_223, list_224, list_225, list_226,
                           list_227, list_228, list_229, list_230, list_231, list_232)
            for PS_point in rows:
                writer.writerow(PS_point)

    # Delete the not useful lines mentioned above to get a nice cleaned CSV file
    with open(output_dir + output_csv) as rf, open(output_dir + output_csv + ".temp", "w") as wf:
        for i, line in enumerate(rf):
            if i != 1 and i != 2:  # Everything but the second and third line
                wf.write(line)

    os.replace(output_dir + output_csv + ".temp", output_dir + output_csv)
