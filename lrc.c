#include<stdio.h>
#include<string.h>
void main()
{
char name[100];
int binary[30][10];
int lrc[30];
int i=0,k,h;
int lim;
int lrccount=0;
int ccount;

printf("Enter your name: ");
scanf("%s",name);
printf("\t***PARITY CHECK* \n");
printf("Character\tASCII \tBINARY VRC \n");
while(name[i]!= 0)
{
int j=0;
int ascii= name[i];
int count=0;
printf(" %c\t       %d    ", name[i],ascii);
while(ascii>0)
{
count+= ascii%2;
ascii/=2;
}
ascii=name[i];
while(ascii !=0)
{
int rem=ascii%2;
binary[i][j]=rem;
j++;
ascii/=2;
}
lim=j;
for(j=j-1;j>=0;j--){
printf("%d",binary[i][j]);
}
if(count%2==0){
printf(" 0 \t ");
}else{
printf(" 1 \t ");
}
printf("\n");
i++;
}
printf("\t\t LRC=");
for(k=lim-1;k>=0;k--)
{
lrc[k]=0;
for(h=0;h<i;h++)
{
lrc[k]+=binary[h][k];
}
if(lrc[k]%2==0)
printf("0");
else
printf("1");
}
for(i=0;i<lim;i++)
{
lrccount+=lrc[i];
}

printf("\n2d of the above is\n ");
ccount=0;
for(i=0;i<=strlen(lrc);i++)
{
	
	if(lrc[i]==1)
	{
		ccount++;
	}}
	if(ccount%2==0)
	{printf("1");}
	else 
	printf("0");
	
}