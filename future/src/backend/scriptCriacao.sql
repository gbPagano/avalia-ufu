INSERT INTO faculdades (nome)
VALUES 
('FACES'),
('FAUED'),
('FACIC'),
('FACOM'),
('FADIR'),
('FACED'),
('FAEFI'),
('FECIV'),
('FEELT'),
('FEMEC'),
('FEQUI'),
('FAGEN'),
('FAMAT'),
('FAMED'),
('FAMEV'),
('FOUFU'),
('IARTE'),
('INBIO'),
('IBTEC'),
('ICIAG'),
('ICBIM'),
('ICENP'),
('ICHPO'),
('INCIS'),
('IERI'),
('IFILO'),
('INFIS'),
('IG'),
('INHIS'),
('ILEEL'),
('IP'),
('IQUFU');


INSERT INTO profs (id_faculdade, nome, descricao, nota)
VALUES 
(32, 'Heidi Grabban', 'nec dui luctus rutrum nulla tellus in sagittis dui vel nisl duis ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti in eleifend quam a odio', 7.30648),
(32, 'Orelie Skipperbottom', 'nisi at nibh in hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent', 5.9788),
(15, 'Petronella Verick', 'in congue etiam justo etiam pretium iaculis justo in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat id mauris vulputate elementum', 9.70991),
(14, 'Seth Mackley', 'velit vivamus vel nulla eget eros elementum pellentesque quisque porta volutpat erat quisque erat eros viverra', 5.55814),
(12, 'Savina Aggio', 'pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit amet sem fusce consequat nulla nisl nunc nisl duis bibendum', 7.4383),
(17, 'Sunny Sproat', 'elit proin risus praesent lectus vestibulum quam sapien varius ut blandit non interdum in ante vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae duis faucibus accumsan odio curabitur', 6.86834),
(8, 'Madalena Blunsom', 'porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut at dolor quis odio consequat varius integer ac leo pellentesque', 4.87878),
(13, 'Margarete Ravelus', 'pellentesque volutpat dui maecenas tristique est et tempus semper est quam pharetra magna ac consequat metus sapien ut nunc vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae mauris viverra diam vitae quam suspendisse potenti nullam porttitor', 6.81341),
(17, 'Kelly Eckery', 'quis justo maecenas rhoncus aliquam lacus morbi quis tortor id nulla ultrices aliquet maecenas leo odio condimentum id luctus nec molestie sed justo pellentesque viverra', 4.30445),
(2, 'Manuel Paramore', 'ante vel ipsum praesent blandit lacinia erat vestibulum sed magna', 8.23379),
(30, 'Alica Greenhall', 'justo in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat id mauris vulputate elementum nullam varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum pellentesque quisque porta', 7.92246),
(7, 'Regan Surgener', 'in purus eu magna vulputate luctus cum sociis natoque penatibus et magnis', 5.38612),
(29, 'Renato Till', 'dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis', 3.82521),
(26, 'Melany Smalles', 'diam erat fermentum justo nec condimentum neque sapien placerat ante nulla justo aliquam quis turpis eget elit sodales scelerisque mauris sit amet eros suspendisse accumsan tortor quis turpis sed ante vivamus tortor', 3.00737),
(14, 'Odilia Conrath', 'nulla eget eros elementum pellentesque quisque porta volutpat erat quisque erat eros viverra', 4.19176);


INSERT INTO disciplinas (id_faculdade, nome, dificuldade)
VALUES
(13, 'Cálculo Diferencial e Integral I', 8),
(13, 'Cálculo Diferencial e Integral II', 8),
(13, 'Cálculo Diferencial e Integral III', 9),
(13, 'Métodos Matemáticos', 8),
(13, 'Estatística', 7),
(13, 'Geometria Analítica', 7),
(13, 'Álgebra Linear', 9),
(9, 'Introdução à Engenharia de Computação', 4),
(9, 'Programação Script', 6),
(9, 'Programação Funcional', 6),
(9, 'Programação Lógica e Inteligência Artificial', 6),
(9, 'Programação Orientada a Objetos', 7),
(9, 'Programação Procedimental', 7),
(9, 'Enriquecimento Instrumental', 6),
(27, 'Física Básica: Mecânica', 7),
(27, 'Física Básica: Eletricidade e Magnetismo', 8),
(9, 'Circuitos Elétricos I', 8),
(9, 'Circuitos Elétricos II', 8),
(9, 'Eletrônica Analógica I', 9),
(9, 'Eletrônica Analógica II', 7),
(9, 'Sistemas Embarcados I', 9),
(9, 'Sistemas Embarcados II', 8),
(14, 'Saúde Coletiva I', 6),
(14, 'Saúde Coletiva II', 7),
(14, 'Saúde Individual I', 7),
(14, 'Saúde Individual II', 7),
(14, 'Das Moléculas aos Tecidos', 9),
(14, 'Dos Tecidos aos Sistemas I', 8),
(14, 'Dos Tecidos aos Sistemas II', 7),
(9, 'Sistemas Digitais', 7),
(9, 'Tecnologias Web e Mobile', 6),
(9, 'Engenharia de Software', 6),
(9, 'Elementos de Sistemas Computacionais', 7),
(9, 'Arquitetura e Organização de Computadores', 7),
(9, 'Sinais e Multimídia', 7),
(9, 'Sistemas Operacionais', 8),
(9, 'Teoria da Computação', 9),
(9, 'Computação Gráfica RV-RA', 6),
(9, 'Robótica', 7),
(9, 'Otimização e Simulação', 7),
(9, 'Redes de Comunicações I', 7),
(9, 'Redes de Comunicações II', 7),
(9, 'Sistemas Computacionais em Tempo Real', 8),
(9, 'Segurança de Sistemas Computacionais', 7),
(9, 'Sistemas Distribuídos', 7),
(5, 'Ciências Sociais e Jurídicas', 6),
(12, 'Administração', 5);

INSERT INTO vinculos_profs_discs (id_prof, id_disc)
VALUES
(8,9),
(4,34),
(3,44),
(12,39),
(12,13),
(9,28),
(6,6),
(12,40),
(4,27),
(13,21),
(3,47),
(12,2),
(8,20),
(6,6),
(9,47),
(11,33),
(4,12),
(15,33),
(2,41),
(14,43),
(15,37),
(4,40),
(5,32),
(8,9),
(7,44),
(9,20),
(1,21),
(7,23),
(7,18),
(6,1),
(12,15),
(10,37),
(2,34),
(9,31),
(12,33),
(1,4),
(15,41),
(14,14),
(4,31),
(9,31),
(13,1),
(2,20),
(7,15),
(6,24),
(13,38),
(11,35),
(8,39),
(14,25),
(15,2),
(15,42),
(7,45),
(8,21),
(7,45),
(1,3),
(2,18),
(11,40),
(7,22),
(9,25),
(3,23),
(10,2),
(9,24),
(15,36),
(3,1),
(7,31),
(7,40),
(6,42),
(12,13),
(3,24),
(15,30),
(11,10),
(5,10),
(4,22),
(14,10),
(5,1),
(15,34),
(6,43),
(13,30),
(5,25),
(2,47),
(15,35),
(15,26),
(3,40),
(6,2),
(11,41),
(13,4),
(12,36),
(3,37),
(10,17),
(13,12),
(4,13),
(14,23),
(15,40),
(12,38),
(6,6),
(3,32),
(6,42),
(15,9),
(7,24),
(7,2);

INSERT INTO reviews (id_prof, id_disc, autor, comentario, nota, dif_disc, upvotes) 
VALUES 
(1, 21, 'btowhey0', 'In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.

Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.', 10, 9, -775),
(11, 33, 'pspottiswoode1', 'Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.

In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.', 1, 1, -995),
(10, 2, 'cmumford2', 'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.

Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.

In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.', 1, 4, 681),
(4, 13, 'hrosenstiel3', 'Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.

Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.', 5, 4, 756),
(7, 2, 'yceillier4', 'Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.

Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.

Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', 2, 10, 981),
(10, 37, 'mshotboult5', 'Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', 6, 7, -43),
(7, 44, 'aoakhill6', 'Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.

Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.

Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.', 3, 9, 383),
(12, 39, 'jabramin7', 'Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.

Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.', 5, 1, 344),
(5, 1, 'uallmond8', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.

Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.

Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', 10, 4, 313),
(3, 44, 'ztortoishell9', 'Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.

Phasellus in felis. Donec semper sapien a libero. Nam dui.', 10, 4, -456),
(5, 32, 'jbloysa', 'Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.

Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.

Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.', 3, 7, 607),
(10, 2, 'htidboldb', 'Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.', 10, 9, 756),
(2, 41, 'gleupoldc', 'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.

Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.

In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.', 8, 2, -866),
(8, 9, 'kspraggsd', 'Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.', 7, 3, 973),
(3, 47, 'eytere', 'Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.', 2, 7, 429),
(2, 34, 'mgrinsteadf', 'Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.

Sed ante. Vivamus tortor. Duis mattis egestas metus.

Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.', 5, 4, -661),
(11, 35, 'lpunyerg', 'In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.

Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.', 2, 1, 127),
(3, 23, 'dthurlowh', 'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', 4, 10, 1),
(9, 28, 'hgillorani', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.

Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.

Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', 2, 8, 481),
(9, 31, 'tgiacomoj', 'Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.

Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', 5, 2, -522),
(2, 20, 'bjays0', 'In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.', 8, 2, 962),
(11, 40, 'gcritchard1', 'Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.', 5, 5, 708),
(9, 47, 'irumke2', 'Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', 9, 3, 801),
(12, 2, 'slongden3', 'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.

Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.', 8, 5, 576),
(15, 30, 'mperrinchief4', 'Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.', 9, 5, -863),
(10, 37, 'djahnke5', 'Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.', 8, 5, -846),
(3, 23, 'cperett6', 'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.

Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.', 2, 8, 591),
(11, 41, 'crennox7', 'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.

Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.', 8, 4, -49),
(6, 1, 'amassy8', 'Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.

Fusce consequat. Nulla nisl. Nunc nisl.

Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.', 1, 1, -689),
(2, 18, 'plie9', 'Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.

Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.', 1, 4, 815),
(15, 2, 'gbefroya', 'Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.

Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.

Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', 6, 3, -463),
(13, 21, 'mluebbertb', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.

Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.

Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', 3, 2, -747),
(2, 47, 'graywoodc', 'Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.

Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', 1, 1, 37),
(8, 20, 'tphuprated', 'Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem.

Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.', 8, 2, -712),
(12, 40, 'mplayere', 'In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet.', 9, 10, -160),
(13, 1, 'aoertzenf', 'Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.

Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.

Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.', 9, 6, 143),
(13, 12, 'tstintong', 'In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.

Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.

Sed ante. Vivamus tortor. Duis mattis egestas metus.', 5, 7, -920),
(6, 6, 'idefewh', 'Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.

Fusce consequat. Nulla nisl. Nunc nisl.

Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum.', 9, 3, 89),
(4, 13, 'hbiffini', 'Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.

Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.

Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.', 7, 4, -823),
(13, 38, 'cgreensidej', 'Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.', 1, 6, 156),
(4, 34, 'kmenneark', 'Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.

Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', 10, 10, -487),
(10, 17, 'ghedgeleyl', 'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.

Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.

In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.', 7, 5, -806),
(12, 33, 'chehlm', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.

Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.

Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', 10, 7, 972),
(8, 39, 'cskylettn', 'Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.

Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.', 6, 8, 254),
(7, 23, 'tchatreso', 'Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.

Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.', 9, 10, 633),
(2, 18, 'akleinpeltzp', 'Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.

Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.', 2, 4, -364),
(1, 4, 'peddlestonq', 'Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.

Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.

Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.', 2, 7, 355),
(4, 12, 'cbresnerr', 'In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.

Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.

Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.', 3, 3, -48),
(1, 3, 'skryszkieciczs', 'Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.', 2, 7, 412),
(2, 18, 'nwellandt', 'Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.', 10, 9, -872);
