void queens(index i)
{
	index j;
	if (promising(i))
		if (i == n) #n개의 퀸을 다 놓았다는 뜻
			print col[1] through col[n];
		else #n개의 퀸 다 안놓은 상황이라 
			for (j=1; j<=ㅜ; j++) {
			col[i + 1] = j
			queens(i + 1);
			}
}

#i가 promising한가에 대한 검사
bool promising(index i)
{
	index k;
	bool switch;
	k = 1;
	switch = ture;
	while (k < i && switch) {
		if (col[i]==col[k] || abs(col[i]-col[k]) == i-k) #컬럼값이 동일 || 대각선의경우는 nonpromising!
			switch = false;
		k++;
	}
	return switch;
}

#호출 
queens(0)
