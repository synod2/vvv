signature= + flag + 입력 메시지 로 전체 메시지가 만들어져서 암호화됨. 
암호화 키는 고정이고, 랜덤 16길이 nonce에 의해 ctr이 만들어짐. 
따라서 동일한 내용을 넣더라도 암호화 결과가 다를 수 있음. 
암호화는 zlib으로 compress한 결과를 암호화. 
이후 전송시에 nonce + 암호화(컴프레스(플래그+메시지)) 를 전송한다. 

복호화시에 nonce 로 활용하는 내용은 앞 32글자. 
복호화 이후 zlib decompress 를 진행한다. 

복호화시 검증하는 부분이 있는데, 
zlib으로 decompress 된 이후 메시지의 플래그를 검증한다.

음, 암호화된 메시지의 암호화 키가 고정이고, nonce 정도만 알수 있는 상태이니까 
문자열을 바꿔가면서 보내어 알아 낼 수 있는 방법도 있을까?
compress 를 시키면 문자열의 순서와는 무관하게 압축되어 전송되는걸로 알고있다. 
(마치 해시처럼.)  암호화시 nonce가 초기화 벡터가 되어 CTR mode 를 적용한다.

CTR 모드를 사용하게 되면 블록암호를 스트림 암호화 방식으로 사용할 수 있게 되는데, 
128비트의 초기화 키를 이용하는것과 같은 셈이다. 

CTR모드의 초기화벡터인 nonce가 고정값일때에 문자열을 알아낼 수 있는 공격기법이 있다.
CTR-MOD를 이용하게 되면 블록마다 증가하는 카운터와 nonce를 결합해 키 스트림을 만들고
해당 키 스트림과 평문 블록을 연산한 결과를 암호문 블록으로 출력한다.
암호화 키의 동일 바이트를 반복 사용하여 암호문을 만들때에 사용한다는 이야기.

따라서, 각 데이터에서 같은 인덱스의 블록들을 모으면
같은 키 스트림을 가지는 암호문 리스트를 얻을 수 있게 된다.

지금같은 경우는 128비트(16바이트) 길이의 키를 반복하여 블록암호처럼 사용한다. 
즉, 128비트짜리 블록마다 특정한 키 스트림이 반복되며, 해당 키 스트림은
nonce + 카운터 로 만들어진다는 것. 

근데 저 방법을 여기에 적용할수 있나 ..?

다시 생각해보자. 이 문제에서 내가 활용할 수 있는것들

1. nonce를 알 수 있다. 
2. 암호화-복호화가 자유롭다 ( 비록 zlib 결과가 나오지만) 
3. zlib 으로 compress 된 문자열의 첫 4바이트는 789C이다. 

정도인데..?
약간 바꿔서 생각하면, nonce는 바뀌지만 계속해서 동일한 평문을 암호화 한다고 볼수도 있디.
그럼 잘만 하면 테이블을 만들어 볼 수도 있는거 아닐까? 블록암호 방식으로 바뀌니까 말이다. 

94	56	de	d7	37	c8	48	a3	cc	35	e5	70	0b	69	c2	a1
86	77	0b	e9	0f	47	7	34	50	70	2c	21	70	ad	a1	64
ae	e2	d5	d9	95	ae	ef	49	c6	cc	b2	b8	7e	ef	9f	60
															
f4	b9	43	60	56	50	8b	97	ff	a9	a2	1a	6a	ab	fb	c2
94	93	b6	ea	4d	37	f5	eb	bb	7	df	62	7d	c8	e9	4e
ad	a7	49	4e	35	94	43	6	eb	99	6f	85	c4	9b	f3	6f
															
96	ec	35	aa	19	d1	8e	f5	8a	f7	52	93	fd	d0	22	be
fd	95	a1	99	7a	30	84	7e	ef	8e	74	b5	f9	50	5	d4
d1	84	43	a4	bd	19	39	a7	c4	33	85	f0	3f	c7	88	6c
															
31	35	27	bd	09	23	c3	0c	00	94	b6	6	f3	6b	ea	5a
b1	df	8b	72	fd	e9	0f	4e	78	5e	2f	c8	37	41	be	ac
53	a6	15	86	b2	35	b2	24	29	73	bb	bd	66	5f	b8	d7



