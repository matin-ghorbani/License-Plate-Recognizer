# License Plate Recognizer
Implement a Iranian license plate recognizer

**I used and trained [Deep Text Recognition Benchmark](https://github.com/clovaai/deep-text-recognition-benchmark.git) on Iranian License Plates on this [dataset](https://github.com/mut-deep/IR-LPR)**

## DTRB Iranian License Plate Recognition
#### I Have a function in `prepare_dataset.py` to convert xml format to DTRB format


### Training Information
|Iteration| Train loss | Valid loss | Best accuracy |
|---------| -------- | --------     | -------- |
|9000|   0.00050   |0.69526        | 80.559 |

### Inferences on testing images:
<table>
  <tr>
    <td><img src="./test_images/00074.jpg"></td>
    <td><img src="./test_images/010.jpg"></td>
    <td><img src="./test_images/02.jpg"></td>
    <td><img src="./test_images/11.jpg"></td>
    <td><img src="./test_images/17.jpg"></td>
  </tr>
  <tr>
    <td>67922111</td>
    <td>68b31699</td>
    <td>28i21255</td>
    <td>12u32211</td>
    <td>63i56855</td>
  </tr>
   <tr>
    <td>@ : ویلچر</td>
    <td>B : ب</td>
    <td>I : ی</td>
    <td>U : ص</td>
    <td>I : ی</td>
  </tr>
</table>

### This is my [License plate recognizer weight](https://drive.google.com/file/d/1-N2uqe1bS0H6TTfLVpLCzlQtTgq7yan3/view?usp=sharing) if you want to test it.