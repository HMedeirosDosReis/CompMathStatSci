#include<string>
#include<vector>
#include<iostream>

struct Palindrome {
    std::string strPalindrome;
    std::string strFront;
    std::string strEnd;
};

using VectorOfVectorOfIntermediate = std::vector<std::vector<Palindrome>>;

std::string findLongestPalindrome(const std::string &strInput) {
    VectorOfVectorOfIntermediate vecVecIntermediate = VectorOfVectorOfIntermediate(strInput.size(), std::vector<Palindrome>(strInput.size() + 1));
    for ( int i = 0; i < strInput.size(); ++ i ) {
        vecVecIntermediate[i][1].strPalindrome = strInput[i];
        vecVecIntermediate[i][1].strFront = "";
        vecVecIntermediate[i][1].strEnd = "";
    }

    for ( int i = 0; i < strInput.size() - 1; ++ i ) {
        if ( strInput[i] == strInput[i + 1 ]) {
            vecVecIntermediate[i][2].strPalindrome = strInput.substr(i, 2 );
            vecVecIntermediate[i][2].strFront = "";
            vecVecIntermediate[i][2].strEnd = "";
        }else {
            vecVecIntermediate[i][2].strPalindrome = strInput[i];
            vecVecIntermediate[i][2].strEnd = strInput[i+1];
        }
    }

    for ( int L = 3; L <= strInput.size(); L += 1 ) {
        for ( int n = 0; n <= strInput.size() - L;  n++ ) {
            size_t findPos;

            Palindrome p2 = vecVecIntermediate[n][L-1];
            p2.strEnd.push_back ( strInput[n + L - 1] );
            findPos = p2.strFront.find_first_of ( p2.strEnd );
            if ( findPos != std::string::npos) {
                auto charFind = p2.strFront[findPos];
                p2.strPalindrome.insert ( p2.strPalindrome.begin(), charFind );
                p2.strPalindrome.push_back ( charFind );
                p2.strFront = p2.strFront.substr ( 0, findPos );
                findPos = p2.strEnd.find ( charFind );
                p2.strEnd = p2.strEnd.substr ( findPos + 1 );
            }

            Palindrome p3 = vecVecIntermediate[n+1][L-1];
            p3.strFront.insert ( p3.strFront.begin(), strInput[n] );
            findPos = p3.strFront.find_first_of ( p3.strEnd );
            if ( findPos != std::string::npos) {
                auto charFind = p3.strFront[findPos];
                p3.strPalindrome.insert ( p3.strPalindrome.begin(), charFind );
                p3.strPalindrome.push_back ( charFind );
                p3.strFront = p3.strFront.substr ( 0, findPos );
                findPos = p3.strEnd.find ( charFind );
                p3.strEnd = p3.strEnd.substr ( findPos + 1 );
            }

            std::vector<Palindrome> vecP{p2, p3};
            int nMaxIndex = 0;
            //for ( int index = 1; index < 2; ++ index ) {
                if ( p3.strPalindrome.length() > p2.strPalindrome.length() ) {
                    nMaxIndex = 1;
                }
            //}
            vecVecIntermediate[n][L] = vecP[nMaxIndex];
        }
    }
    return vecVecIntermediate[0][strInput.size()].strPalindrome;
}

void Test_findLongestPalindrome()
{
    {
        std::string strTestCase("a");
        auto strPalindrome = findLongestPalindrome ( strTestCase );
        std::cout << "Test case " << strTestCase << ", result " << strPalindrome << std::endl;
    }

    {
        std::string strTestCase("aa");
        auto strPalindrome = findLongestPalindrome ( strTestCase );
        std::cout << "Test case " << strTestCase << ", result " << strPalindrome << std::endl;
    }

    {
        std::string strTestCase("abca");
        auto strPalindrome = findLongestPalindrome ( strTestCase );
        std::cout << "Test case " << strTestCase << ", result " << strPalindrome << std::endl;
    }

    {
        std::string strTestCase("abbac");
        auto strPalindrome = findLongestPalindrome ( strTestCase );
        std::cout << "Test case " << strTestCase << ", result " << strPalindrome << std::endl;
    }

    {
        std::string strTestCase("abcdefghijkjhgfed");
        auto strPalindrome = findLongestPalindrome ( strTestCase );
        std::cout << "Test case " << strTestCase << ", result " << strPalindrome << std::endl;
    }

    {
        std::string strTestCase("character");
        auto strPalindrome = findLongestPalindrome ( strTestCase );
        std::cout << "Test case " << strTestCase << ", result " << strPalindrome << std::endl;
    }

    {
        std::string strTestCase("GEEKS FOR GEEKS");
        auto strPalindrome = findLongestPalindrome ( strTestCase );
        std::cout << "Test case " << strTestCase << ", result " << strPalindrome << std::endl;
    }
}

int main()
{
    Test_findLongestPalindrome();
    return 1;
}