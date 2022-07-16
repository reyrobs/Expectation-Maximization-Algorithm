<div align="center">
<div id="top"></div>
<h2 align="center">Expectation Maximization Algorithm</h3>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-description">Project Description</a>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">References</a></li>
  </ol>
</details>

## Background

The EM algorithm is commonly used for estimating the best parameters which would represent a given dataset. It is an elegant and powerful method for ﬁnding maximum likelihood solutions for models with latent variables. It consists of two main steps, namely the *E* step (expectation step) and *M* step (maximization step). In the *E* step, the current parameter values are used to evaluate the posterior probabilities, or responsibilities. These probabilities are then used in the *M* step, such that to re-estimate the corresponding means and covariances. The algorithm is said to be complete when either the log likelihhod or parameters of the model have converged. A more in depth explanation of the EM algorithm can be found in the Bishop book [[1]](#1). An example of an application of the EM algorithm is with the popular clustering K-means algorithm. 

<p align="right">(<a href="#top">back to top</a>)</p>

## Model used for the EM algorithm

![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/model_diagg.png?raw=true)

![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/problem_desc.png?raw=true)

## Implementation of the EM algorithm

![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/algo_description.png?raw=true)


<p align="right">(<a href="#top">back to top</a>)</p>

## Results obtained for different values of K

### Results for K=2

![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/K_2_Gau.png?raw=true)
&emsp;&emsp;&emsp;&emsp;
![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/K_2_Po.png?raw=true)
&emsp;&emsp;&emsp;&emsp;

### Results for K=3
![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/K_3_Gau.png?raw=true)
&emsp;&emsp;&emsp;&emsp;
![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/K_3_Po.png?raw=true)
&emsp;&emsp;&emsp;&emsp;

### Results for K=4
![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/K_4_Gau.png?raw=true)
&emsp;&emsp;&emsp;&emsp;
![alt text](https://github.com/reyrobs/Expectation-Maximization-Algorithm/blob/main/images/K_4_Po.png?raw=true)
&emsp;&emsp;&emsp;&emsp;

<p align="right">(<a href="#top">back to top</a>)</p>

## Interpretation of results

When we have a value of K=3, the Gaussian distributions seem to be more equally distributed among all the points, although the blue cluster does appear to contain more points than the others. If we consider the points by themselves, i.e without their corresponding clusters, we can already point out 3 possible clusters already, namely the ones that have been created after running our EM algorithm. Therefore this is why we believe that setting a value of K=3 resulted in the most successful set of results, or at least the ones that make the most sense intuitively. Looking at the Poisson distribution for K=3, we essentially obtain a similar set of results, being that the points are more or less equally distributed among the different Poisson distributions. 
<br>
<br>
<br>
Finally when setting a value of K=4, the results we obtain aren't very representative of what is happening. If we look at the points on the upper left of the diagram, they are shared between the red and green cluster which creates contour plots of their Gaussian distributions that are intertwined with each other, when in reality they should belong to the same cluster and hence be attributed to only one Gaussian distribution. The reason this is happening is because we are explicitly telling our EM algorithm that it should assign the points to 4 clusters, and hence it performs a "forced" assignment so to speak, which doesn't end up as a very successful result, at least we believe that to be the case. The same point can be said for the Poisson distributions.

<!-- CONTACT -->
## Contact

Robert Rey - [LinkedIn](https://www.linkedin.com/in/robert-rey-36689a103/)

Project Link: [Athlete Classification](https://github.com/reyrobs/Expectation-Maximization-Algorithm)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## References
<a id="1">[1]</a> 
Bishop C.M.B, 2006, Mixture Models and EM, *Pattern Recognition and Machine Learning*, Springer, 423-455. 


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
