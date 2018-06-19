--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.8
-- Dumped by pg_dump version 9.6rc1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: initiates; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE initiates (
    id integer NOT NULL,
    name character varying(50),
    phone_number character varying(10),
    initiate_problem character varying(1024),
    "timestamp" timestamp with time zone DEFAULT now() NOT NULL
);


--
-- Name: initiates_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE initiates_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: initiates_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE initiates_id_seq OWNED BY initiates.id;


--
-- Name: register_surgeons; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE register_surgeons (
    id integer NOT NULL,
    name character varying(50),
    area character varying(255),
    phone_number character varying(10),
    "timestamp" timestamp with time zone DEFAULT now() NOT NULL
);


--
-- Name: register_surgeons_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE register_surgeons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: register_surgeons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE register_surgeons_id_seq OWNED BY register_surgeons.id;


--
-- Name: reportsurgeons; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE reportsurgeons (
    id integer NOT NULL,
    opt_name character varying(50),
    phone_number character varying(10),
    surgeons_name character varying(50),
    area character varying(255),
    report_problem character varying(1024),
    "timestamp" timestamp with time zone DEFAULT now() NOT NULL
);


--
-- Name: reportsurgeons_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE reportsurgeons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reportsurgeons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE reportsurgeons_id_seq OWNED BY reportsurgeons.id;


--
-- Name: roles; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE roles (
    id integer NOT NULL,
    name character varying(80),
    description character varying(255)
);


--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE roles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE roles_id_seq OWNED BY roles.id;


--
-- Name: roles_users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE roles_users (
    user_id integer,
    role_id integer
);


--
-- Name: surgeons; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE surgeons (
    id integer NOT NULL,
    name character varying(50),
    id_number character varying(50),
    area character varying(255),
    phone_number character varying(10),
    standard character varying(10),
    category character varying(10)
);


--
-- Name: surgeons_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE surgeons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: surgeons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE surgeons_id_seq OWNED BY surgeons.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE users (
    id integer NOT NULL,
    email character varying(50) NOT NULL,
    password character varying(100),
    disabled boolean,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    updated_at timestamp with time zone DEFAULT now()
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE users_id_seq OWNED BY users.id;


--
-- Name: initiates id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY initiates ALTER COLUMN id SET DEFAULT nextval('initiates_id_seq'::regclass);


--
-- Name: register_surgeons id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY register_surgeons ALTER COLUMN id SET DEFAULT nextval('register_surgeons_id_seq'::regclass);


--
-- Name: reportsurgeons id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY reportsurgeons ALTER COLUMN id SET DEFAULT nextval('reportsurgeons_id_seq'::regclass);


--
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY roles ALTER COLUMN id SET DEFAULT nextval('roles_id_seq'::regclass);


--
-- Name: surgeons id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY surgeons ALTER COLUMN id SET DEFAULT nextval('surgeons_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


--
-- Data for Name: initiates; Type: TABLE DATA; Schema: public; Owner: -
--

COPY initiates (id, name, phone_number, initiate_problem, "timestamp") FROM stdin;
\.


--
-- Name: initiates_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('initiates_id_seq', 12, true);


--
-- Data for Name: register_surgeons; Type: TABLE DATA; Schema: public; Owner: -
--

COPY register_surgeons (id, name, area, phone_number, "timestamp") FROM stdin;
11	Thabo Mngambi	bizana	0782788473	2017-07-23 07:09:24.491747+00
12	Andile Makalima	Cape town	0789442513	2017-08-12 12:15:04.415448+00
13	sintu	butteworth	0624215327	2017-11-06 14:58:14.108786+00
14	Mzimasi Zitha	Zingonyameni A/A,Mount Fletcher	0781445512	2017-11-06 17:41:07.160516+00
15	solomzi ndabeni	Stilfontein duff scott hospital as a Security office	0630023037	2017-12-04 13:29:58.272684+00
16	Andile Makalima	Western cape	0632183840	2017-12-10 23:07:29.46061+00
17	Andile Makalima	Western cape	0632183840	2017-12-10 23:11:05.217456+00
18	MKHUSELI  MINI	KING WILLIAMS TOWN	0826901184	2017-12-24 00:10:49.775961+00
19	willem Armoed	power ville	0837183021	2018-01-19 16:26:00.486149+00
20	Lonwabo Ngxowayizali	Ntabankulu	0789107243	2018-04-15 11:56:00.003396+00
\.


--
-- Name: register_surgeons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('register_surgeons_id_seq', 20, true);


--
-- Data for Name: reportsurgeons; Type: TABLE DATA; Schema: public; Owner: -
--

COPY reportsurgeons (id, opt_name, phone_number, surgeons_name, area, report_problem, "timestamp") FROM stdin;
15	julia	0763210573	charlie	winterveld	they take children from different townships in Johannesburg and pretoria,without their parents permission and later force the boys to give out their parent's phone numbers.They later call the parents and inform them that their children came to their school and start to demand money.I personally helped to relocate three boys with their family today when I was on duty after they ran away from the school.I doubt the school is registered	2018-05-15 18:41:58.775081+00
\.


--
-- Name: reportsurgeons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('reportsurgeons_id_seq', 15, true);


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: -
--

COPY roles (id, name, description) FROM stdin;
\.


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('roles_id_seq', 1, false);


--
-- Data for Name: roles_users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY roles_users (user_id, role_id) FROM stdin;
\.


--
-- Data for Name: surgeons; Type: TABLE DATA; Schema: public; Owner: -
--

COPY surgeons (id, name, id_number, area, phone_number, standard, category) FROM stdin;
1	Zanovuyo Tshangane	7206235994086	Lower Ntafufu A/A Lusikisiki	0796834465	12	TS
2	Gunuza Flawa	7610855002086	Lower Ntafufu A/A Lusikisiki	0729181334	7	TS
3	Siyabonga Ngcingolo 	7510107631088	Goso Forest A/A Lusikisiki	0734965735	12	TS
4	Mveliso Guleni	7610066080085	Qoqo A/A Fagstaff	0834901125	7	TS
5	Zwelethemba Dulaze 	6811245053081	Hombe A/A Lusikisiki	0784265188	12	TS
6	Gcinikhaya Hiliza	8203106477088	Hombe A/A Lusikisiki	0782558993	7	TS
7	Malindela Mjongwa 	\N	Tshonya A/A Lusikisiki	0710508865	2	TS
8	Sibusisi Khwanya	7506136017083	Mantlaneni A/A Fagstaff	0736103557	8	TS
9	Nsikelelo Mabhena 	7910106039087	Mhwaleni A/A Lusikisiki	0837182942	12	TS
10	Ntandazo Mzikiza 	7512225936084	Lambasa  A/A Lusikisiki	0730662857	8	TS
11	Zandisile Madlokolwane 	6003156324087	Xurana  A/A Lusikisiki	0739857290	6	TS
12	Lizo Somtsewu	6306066839080	Dudumeni A/A Flagstaff	0737146869	8	TS
13	Zukile Smtsewu	8006176039088	Madokwe A/A Flagstaff	0732331979	7	TS
14	Khanyile Somtsewu	8607175907082	Mfundisweni A/A Flagstaff	0781092566	9	TS
15	Zwelihle Alfred Goya	8704025932057	Mfundisweni A/A Flagstaff	0785775182	M+4	TS
16	Ayanda Tapelo 	\N	Mfundisweni A/A Flagstaff	0825127659	11	TS
17	Susiso Sopo	6803236063088	Dumeni A/A Flagstaff	0719786518	11	TS
18	Lungisa Vatsha 	9106166131082	Mfundisweni A/A Flagstaff	0788200439	11	TS
19	Thobela	8910048042083	\N	0715268969	\N	TS
20	Molisi Sinukelo	7711035509087	\N	\N	\N	TS
21	Thobintetho Mhleni	\N	\N	\N	\N	TS
22	Zolisile Ndlobeni 	\N	\N	\N	\N	TS
23	M. Mkono	8105035529089	Mdlankomo Location	0733191687	11	TS
24	S. Manzana	8408115935089	Mangwaneni Location	0783769625	10	TS
25	B. Mncele	8004145724088	Mangwaneni Location	0788351409	11	TS
26	S. Ntshona	9006015805086	Mdlankomo Location	0734226670	11	TN
27	A. Fuma	6812156278089	Misty Mount Location	0739292692	8	TS
28	M. Mpukane	7912156148081	Misty Mount Location	0738467891	5	TN
29	S. Mzamane	8104046002087	Gomolo A/A	0786465475	11	TS
30	S. Mbina	8509115670087	Gxulu Location	0733554513	12	TS
31	M. Sidlayiya	8509115670087	Buntingville Location	0760441623	8	TS
32	T. Maphipha	\N	Gxulu Location	0781058225	12	TN
33	S. Mpukwana	8803076286086	Gomolo A/A   	\N	11	TN
34	S. Naki	9002225844080	Gomolo A/A   	0719003447	11	TN
35	S. Qabaqaba	8508066574708	Gomolo A/A   	0781334129	11	TN
36	S. Dlubeka	7602175730080	Gomolo A/A   	0717494140	6	TN
37	M. Goqweni	\N	Mangwaneni A/A	0738864670	6	TN
38	Z. Tshangana	7210623934086	Nomvalo PSJ	0796834465	12	TS
39	N. Ntlanganisela	7610266616086	Mthumbana PSJ	0783450344	12	TS
40	M. Mthokwana	6311106074086	Caguba A/A	0787195299	11	TS
41	M. Ngcingolo	7510107631088	Qabekwana A/A	0734905735	12	TS
42	M. Flawa	7610055892086	Thaleni A/A	0726181334	9	TS
43	Q. Siyongwana	\N	\N	0837560878	\N	TN
44	N. Mzingeli	\N	\N	0732352814	\N	TS
45	S Kholwane 	\N	\N	0731784532	\N	TS
46	T. Matshonyane	\N	\N	0781467826	\N	TS
47	F. Guntsu	\N	\N	0730368342	\N	TS
48	P. Faltein	\N	\N	0839531193	\N	TS
49	K. Kotyi	\N	\N	0731622053	\N	TN
50	M.E. Dlulani	\N	\N	0713497590	\N	TS
51	J. Kholwane	\N	\N	0733517837	\N	TS
52	S. Mangqasana	\N	\N	0838729701	\N	TS
53	S. Mafumbula	\N	\N	0834907720	\N	TS
54	S. Nongogo	\N	\N	0742955841	\N	TS
55	M. Simata	\N	\N	0839858211	\N	TN
56	M. Mbunga	\N	\N	0782075208	\N	TS
57	M. Mavuthulana	\N	\N	0735138348	\N	TS
58	J.J. Mkhefelele	\N	\N	0734841949	\N	TS
59	S. Guntsu	\N	\N	0732530136	\N	TS
60	J. Guntsu	\N	\N	0836935587	\N	TS
61	M. Mpohlo	\N	\N	0736608095	\N	TS
62	M. Ndlobeni	\N	\N	0731680470	\N	TS
63	S. Ncume	\N	\N	0739628894	\N	TS
64	Gugushe	\N	\N	0728773144	\N	TS
65	S. Bholobholo	8103246037086	Nogaga Location	\N	\N	TS
66	Sipilinga Matshiselo	5712255917085	Sulunkama	\N	\N	TS
67	Nyaniso Gwayi	8608106376082	Kwam	\N	\N	TS
68	Mptizeli Matyumza	6103315744085	Tyira	\N	\N	TS
69	Phethile Fana	5404115149089	Ngxakolo	\N	\N	TS
70	Zakhele Ntlebi	5501055875084	Mvumelwano	0787979852	\N	TS
71	Ayanda Monanga	7907075893080	Tina Falls	\N	\N	TS
72	Shumzana Godola	5709175901082	Blackhill	0737803613	\N	TS
73	Mawele Mfuneko	7607015746089	Mpindweni	\N	\N	TS
74	Sangcethe Vulelo	6401115934089	Sikhobeni	\N	\N	TS
75	Isark  Marlouw	5512315201086	Graaff Reinet	\N	\N	TS
76	Dasi Tiyo	4206163593087	Graaff Reinet	\N	\N	TN
77	MK. Jack	5708065764089	Graaff Reinet	\N	\N	TS
78	Adries Oopatjie	350502509089	Graaff Reinet	\N	\N	TN
79	Mvuleni Mahoza	700506590080	Graaff Reinet	0847548715	\N	TN
80	Zoyisile Kulumani	8209125213081	Klipplaat	0716472217	8	TN
81	Thembalethu Sdonca	7711155588085	Klipplaat	\N	11	\N
82	Zinakile Singeni	4909045225081	Klipplaat	0728446998	1	TN
83	Stanley Deshu	5205115648080	Klipplaat	0735846544	8	TN
84	Zanoxolo popo	7210293315087	Kliplaat	0840141983	8	TN
85	Bhongo Rhaliso	\N	\N	\N	10	TN
86	Joe Kobe	8608023188089	Steytlerville	0710231312	10	TN
87	Zamuxolo 	720730355081	Steytlerville	\N	7	TN
88	Nokrayo Hitlana	4001016994084	Debera	0735086595	\N	TS
89	Mluleki Ngqame	3806125220084	Mjanyana	0837157234	\N	TS
90	Mzolisi Fadana	4706235631080	Gqobonco	0826872840	\N	TS
91	Tatana Sangxala	5004125156080	Luhewini	0786418431	\N	TS
92	Melikhaya Sangxala	771035009088	Luhewini	0787401189	\N	TS
93	Shilika Ndude	1901215049089	Ngacu	0736542723	\N	TS
94	Thanduxolo Ndude	7006166434084	Ngcacu	0736542723	\N	TS
95	Ndimphiwe Gulwa	7208235681089	Bodini	0823770298	\N	TS
96	Tyaphile Goba	2910065097089	Gubenxa	0844735644	\N	TS
97	Anivuyi Goba	7711035857086	Gubenxa	0738013372	\N	TS
98	Mondli Mxhobo	4406084149081	Qebe	0785482906	\N	TS
99	Jongixolo Bobotyane	6503126114088	Upper Gqaga	0733551314	\N	TS
100	Malinge Bonga	8704096114086	Gqotyini	0782055686	\N	TS
101	Sakhele Qandashe	7403105668082	Qebe	0787108476	\N	TS
102	Thembeni Baliso	5403295735089	Upper Gqaga	0782057923	\N	TS
103	Ndoyisile Lengisi	4108015106088	Upper Gubenxa	0839784184	\N	TS
104	Mvelisi Lengisi	5902145879088	Upper Gubenxa	0766116975	\N	TS
105	Malusi Baliso	7902045634086	Upper Gqaga	0782815926	\N	TS
106	Malusi Baliso	7902045634086	Upper Gqaga	0712701546	\N	TS
107	Lubabalo Nojingxa	3110115095089	Tsalaba	\N	\N	TS
108	Mlandeli Nogemane	\N	Xonya	0735423279	\N	TS
109	Buza Ndude 	7306106748084	Quluqu	0780105596	\N	TS
110	Kholekile Cokoto	7503225723085	Mount Ayliff	0710232651	\N	TS
111	Xolani Mota	8203015656087	Mount Ayliff	0739775895	\N	TS
112	Zola Zungula	5507165804088	Mount Ayliff	0786071601	\N	TS
113	Thuso Tshayisa	6601255949082	Mount Ayliff	0825884635	\N	TS
114	Siyabonga Cokoto	7506096130082	Mount Ayliff	0762096001	\N	TS
115	Ndumiso P. George	7709246074081	Mount Ayliff	0795671520	\N	TS
116	Sifiso Zoleka	8508015992088	Bizana	0787921069	\N	TS
117	Banele Njomi	8403126213089	Bizana	0782148102	\N	TS
118	Monde Z. Chutshela	7306026346080	Bizana	0835224015	\N	TS
119	Asanda Faku	8506086423084	Bizana	0838700312	\N	TN
120	Ndzima Rambo Jam-jam	\N	Bizana	0732616683	\N	TS
121	Madoda Mandi	\N	Bizana	\N	\N	TN
122	Makhosi Mdibi	8709066055087	Bizana	\N	\N	TN
123	Siphamandla Madikizela	8502026702081	Bizana	0839682867	\N	TS
124	Daluvuyo D. Madikizela	8005125923087	Bizana	0785304010	\N	TN
125	Sabata Nqala	5811165937082	Bizana	\N	\N	TN
126	Zanethemba Mbukhwe	8501216030089	Bizana	\N	\N	TN
127	Mboli Fundile Ngejana	7008106228089	Bizana	\N	\N	TN
128	Ngalonkulu P. Luvuyo	6812115786081	MT. Frere	0736752339	\N	TN
129	Ndongeni Sibongile	7001285872082	MT. Frere	0769145777	\N	TN
130	Mxinwa  Mondli Melusi	8406185611085	MT. Frere	0838920616	\N	TS
131	Ngongoma M. Vuyani	5702285971087	MT. Frere	0727967481	\N	TS
132	Makaula Cyail Zimase	8308205918088	MT. Frere	0791718231	\N	TS
133	Nokwabuza Nokhwabuza	9002256029088	MT. Frere	0839996333	\N	TS
134	Mbathane Maganise	4908145686085	MT. Frere	0826639190	\N	TS
135	Manelisi Nxabi	\N	MT. Frere	0782182892	\N	TS
136	Thulasizwe Mdiko	6311025891081	MT. Frere	0842607092	\N	TS
137	Bulelani Mbambeni	7012066092089	MT. Frere	0796677212	\N	TS
138	Fikile Giwu	\N	MT. Frere	0726952704	\N	TS
139	Zama Qulu	\N	MT. Frere	0825242925	\N	TS
140	Mzameni Mbengi	7304166073089	MT. Frere	0731369749	\N	TN
141	Ntsikelelo Mabhoza                                	7504175924087	Dimbaza	0730724173	\N	\N
142	Bekwa Fuzile	5301018028081	Mzintsane	0835753769	\N	\N
143	Faleni Wilton	2802125307089	Dimbaza	\N	\N	\N
144	Krweqe Eric	5709235913085	Nakani	0793808290	\N	\N
145	Sipho Nto	4101285161081	Mamata	\N	\N	\N
146	Dabi James	\N	\N	\N	\N	\N
147	Lucingo Mthobeli	5307225747089	Madakeni	0723809071	\N	\N
148	Dumisani Bobo	\N	Moddle Drift	\N	\N	\N
149	Vayo   F.                                   	\N	Bhonke	0734673135	\N	\N
150	Koti	\N	Ncemera	\N	\N	\N
151	Narks Makahla	\N	Qumrha	0731317066	\N	\N
152	Xolani Luphongolo	\N	Dimbaza	\N	\N	\N
153	Thozamile Rhini	\N	Dimbaza	\N	\N	\N
154	Samkelo Dyantjie	\N	Dimbaza	\N	\N	\N
155	Xolile Salakutyela	\N	Dimbaza	\N	\N	\N
156	Thembile Mpehla	\N	Dimbaza	\N	\N	\N
157	Simphiwe Royi	\N	Dimbaza	\N	\N	\N
158	Makhira N.	\N	Dimbaza	\N	\N	\N
159	Mjuleni Zingisa	\N	Dimbaza	\N	\N	\N
160	Mfunda Maphahla	\N	Dimbaza	\N	\N	\N
161	Ntanyoza Z.	\N	Dimbaza	\N	\N	\N
162	Eric  Kutu	\N	Dimbaza	\N	\N	\N
163	Anele Ntentelezo	\N	Dimbaza	\N	\N	\N
164	X. Koti	\N	Tyutyu	0824290592	\N	\N
165	M. Damba	\N	Madliki	0731983247	\N	\N
166	L. Zekani	\N	Mxhalanga	0836939385	\N	\N
167	D. Sinuka	\N	Nonibe Tamara	0737996104	\N	\N
168	N. Mango	\N	Ramnyiba	\N	\N	\N
169	M. Mdodiso	\N	Ethembeni	0782763077	\N	\N
170	G. Vika	\N	B/Post	0406361117	\N	\N
171	M. Retshe	\N	Frankfort	0832042898	\N	\N
172	M. Maboza	\N	Dimbaza	0732770227	\N	\N
173	S. Nto	\N	Mamata	0786463993	\N	\N
174	Tutu Madoda	\N	Mt Coke	\N	\N	\N
175	Themba Nanto	\N	Zwelitsha zone 9	\N	\N	\N
176	Mlindeli Xongo	\N	Mlakalaka	\N	\N	\N
177	Siseko Dlabantu	\N	Zwelitsha zone 	\N	\N	\N
178	Thembinkosi Gulubela	\N	Phakamisa	\N	\N	\N
179	M. Peter	\N	Zwelitsha 	\N	\N	\N
180	T. Msadu	\N	Zwelitsha 	\N	\N	\N
181	Lindile Tsili	\N	Phakamisa	\N	\N	\N
182	Zamile Ndyebi	\N	Phakamisa	\N	\N	\N
183	Mthobeli Dingaan	\N	Zwelitsha zone 4	\N	\N	\N
184	S. Mazantsana	\N	Tshabo	\N	\N	\N
185	N. Myoli 	\N	Ndakana	\N	\N	\N
186	V. Gayimani 	\N	Border Post	\N	\N	\N
187	L. Rhetshe	\N	Frankfort	\N	\N	\N
188	Z. Zwelitsha 	\N	Thembeni	\N	\N	\N
189	N. Singilizwe	\N	Luphondweni	\N	\N	\N
190	L. Vingqi	\N	Luzana(kwazidenge)	0765920079	\N	\N
191	Madodeni Holiday	\N	Cumakala(Mlungisi T/ship)	0844582404	\N	\N
192	Z. Ngxokela	\N	Cathcart	0739078071	\N	\N
193	L. Dingaan	\N	Cathcart	0733084173	\N	\N
194	T. Gwazana	\N	Cathcart	0780141538	\N	\N
195	Zukubo Mayalo	\N	Qoboqobo	0714793927	\N	\N
196	Yolandile	\N	Qoboqobo	0838774596	\N	\N
197	Thembela Booi	\N	Qoboqobo	0710644763	\N	\N
198	Khululekile Matiwane	\N	Qoboqobo	0799553154	\N	\N
199	Phumlani Nojazi	\N	Kwamasincedane	0784935330	\N	\N
200	Thembalethu Gwane	\N	Kwamasincedane	0784754470	\N	\N
201	Simnikiwe	\N	Qoboqobo	0833288867	\N	\N
202	Xhathazana T.	\N	Kwamasincedane	0787343322	\N	\N
203	Mtukanyile	\N	Qoboqobo	0747651317	\N	\N
204	Thousand Makhuphula	\N	Newlands	0786427778	\N	\N
\.


--
-- Name: surgeons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('surgeons_id_seq', 204, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY users (id, email, password, disabled, created_at, updated_at) FROM stdin;
1	matthew@opendata.durban	$5$rounds=535000$SsdVL1ZP/SExcf5D$BLu1qIjTUg.oa2epqz3GFvNOxg0cFErDdeJU1MrAk.A	f	2017-02-27 13:01:32.229612+00	2017-02-27 13:01:32.229612+00
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('users_id_seq', 1, true);


--
-- Name: initiates initiates_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY initiates
    ADD CONSTRAINT initiates_pkey PRIMARY KEY (id);


--
-- Name: register_surgeons register_surgeons_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY register_surgeons
    ADD CONSTRAINT register_surgeons_pkey PRIMARY KEY (id);


--
-- Name: reportsurgeons reportsurgeons_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY reportsurgeons
    ADD CONSTRAINT reportsurgeons_pkey PRIMARY KEY (id);


--
-- Name: roles roles_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY roles
    ADD CONSTRAINT roles_name_key UNIQUE (name);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- Name: surgeons surgeons_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY surgeons
    ADD CONSTRAINT surgeons_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_initiates_timestamp; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_initiates_timestamp ON public.initiates USING btree ("timestamp");


--
-- Name: ix_register_surgeons_timestamp; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_register_surgeons_timestamp ON public.register_surgeons USING btree ("timestamp");


--
-- Name: ix_reportsurgeons_timestamp; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_reportsurgeons_timestamp ON public.reportsurgeons USING btree ("timestamp");


--
-- Name: ix_users_created_at; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_users_created_at ON public.users USING btree (created_at);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: roles_users roles_users_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY roles_users
    ADD CONSTRAINT roles_users_role_id_fkey FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE;


--
-- Name: roles_users roles_users_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY roles_users
    ADD CONSTRAINT roles_users_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

