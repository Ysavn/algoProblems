//Fisher-Yates shuffling
#include<iostream>
#include<vector>
using namespace std;
void swap(int & a,int & b){
	int tmp = a;
	a = b;
	b = tmp;
}
void shuffle(vector<int> & v){

	int n = v.size();
	for(int i=n-1;i>0;i--){
		int j = rand()%(i+1);
		swap(v[i],v[j]);	
	}
	// the idea here is to imagine a hat with all the numbers
	// you randomly pick one number and arrange it one at a time from end
	// resulting in every permuation having equal probability
}
void print(vector<int> & v){
	for(int i=0;i<v.size();i++){
		cout<<v[i]<<' ';
	}
	cout<<endl;
}
int main(){

	// to generate a random permuatation of a given array without duplicates
	vector<int> v {2,3,1,5};
	cout<<"Original: ";
	print(v);
	shuffle(v);
	cout<<"Shuffled: ";
	print(v);
	return 0;
}

