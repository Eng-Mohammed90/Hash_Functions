#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
////////////////////////////////////////////////////////// 
    // طباعة أكثر رقم متكرر
    // int n;
    // cin >> n;
    // map <int, int> freq;
    // for (int i = 0; i < n; i++){
    //     int x;
    //     cin >> x;
    //     freq[x]++;
    // }
    // int maxfreq = 0;
    // int answer = 0;
    // for ( auto p : freq){
    //     if (p.second > maxfreq){
    //         maxfreq = p.second;
    //         answer = p.first;
    //     }
    // }
    // cout << answer << "/n"; 
    
////////////////////////////////////////////////////////////////
// طباعة عدد مرات تكرار أكثر عنصر مكرر
    // int n;
    // cin >> n;

    // map <int, int> freq;
    // for (int i = 0; i < n; i++){
    //     int x;
    //     cin >> x;
    //     freq[x]++;
    // }
    // int maxvalue = 0;
    // for (auto p : freq){
    //     if( p.second > maxvalue){
    //         maxvalue = p.second;
    //     }
    // }
    // cout << maxvalue << endl;
//  ////////////////////////////////////////////////
// نفس الاول أكثر عنصر تكرر و نفس الحل
    // int n;
    // cin >> n;
    // map <int, int> freq;
    // for(int i= 0; i < n; i++){
    //     int x;
    //     cin >> x;
    //     freq[x]++;
    // }
    // int maxfreq = 0;
    // int answer;
    // for(auto p : freq){
    //     if (p.second > maxfreq){
    //         maxfreq = p.second;
    //         answer = p.first;
    //     }
    // }
    // cout << answer << endl;
//  ////////////////////////////////////////
// two pointers to find if there are two numbers in the list have there sum = target.
    // int n;
    // cin >> n;
    // vector <int> v(n);
    // for(int i = 0; i < n; i++){
    //     cin >> v[i];
    // }
    // int target;
    // cin >> target;

    // int left = 0;
    // int right = n-1;
   
    // while(left < right){
    //     int sum = v[left] + v[right];

    //     if(sum == target){
    //         cout << "YES\n";
    //         return 0;
    //     }else if (sum < target){
    //         left++;
    //     }else{
    //         right--;
    //     }

    // }
    // cout << "NO\n";
    //  ////////////////////////////////////////
// نفس اللي فوق بس هان بحيب كم عدد الأزواج التي اجتازت الاختبار
//     int n;
//     cin >> n;
//     vector <int> v(n);

//     for(int i = 0; i < n ; i++){
//         int x;
//         cin >> x;
//         v[i] = x;
//     }

//     int target ;
//     cin >> target;
//     int count = 0;

//     int left = 0;
//     int right = n-1;

//     while(right > left){
//         int sum = v[left] + v[right];
//         if(sum == target){
//             count++;
//             left++;
//             right--;
//         }else if(sum < target){
//             left++;
//         }else{
//             right --;
//         }
// }
// cout << "count is: " << count << "\n";
// ////////////////////////////////////////
// same as above but using map
    
    // int n;
    // cin >> n;

    // vector<int> v(n);

    // for (int i = 0; i < n; i++) {
    //     cin >> v[i];
    // }

    // long long target;
    // cin >> target;

    // int left = 0;
    // int right = n - 1;
    // long long count = 0;

    // while (left < right) {
    //     long long sum = (long long)v[left] + v[right];

    //     if (sum < target) {
    //         left++;
    //     }
    //     else if (sum > target) {
    //         right--;
    //     }
    //     else {
    //         if (v[left] == v[right]) {
    //             long long k = right - left + 1;
    //             count += k * (k - 1) / 2;
    //             break;
    //         }

    //         long long leftCount = 1;
    //         long long rightCount = 1;

    //         while (left + 1 < right &&
    //                v[left] == v[left + 1]) {
    //             leftCount++;
    //             left++;
    //         }

    //         while (right - 1 > left &&
    //                v[right] == v[right - 1]) {
    //             rightCount++;
    //             right--;
    //         }

    //         count += leftCount * rightCount;

    //         left++;
    //         right--;
    //     }
    // }

    // cout << count << "\n";
    // تذكّر أهم قاعدة: لا تحفظ حركة المؤشرين فقط，
    // بل افهم لماذا نحرّك كل واحد منهما، وانتبه للتكرارات عندما نعدّ الأزواج.
    return 0;
}
