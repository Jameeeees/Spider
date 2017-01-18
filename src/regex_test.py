#!/usr/bin/env python
# coding=utf-8
import re

sample = '''
<td>ѧ��</td><td>ѧ��</td><td>�γ̴���</td><td>�γ�����</td><td>�γ�����</td><td>�γ̹���</td><td>ѧ��</td><td>����</td><td>ƽʱ�ɼ�</td><td>���гɼ�</td><td>��ĩ�ɼ�</td><td>ʵ��ɼ�</td><td>�ɼ�</td><td>���ޱ��</td><td>�����ɼ�</td><td>���޳ɼ�</td><td>ѧԺ����</td><td>��ע</td><td>���ޱ��</td><td>�γ�Ӣ������</td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>0BH04227</td><td>JAVA Web����</td><td>���޿�</td><td>&nbsp;</td><td>3.0</td><td>   4.00</td><td>92</td><td>&nbsp;</td><td>92</td><td>96</td><td>93</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�����ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>0RL04911</td><td>UML����Ӧ��</td><td>ѡ�޿�</td><td>&nbsp;</td><td>2</td><td>   4.00</td><td>97.5</td><td>&nbsp;</td><td>89</td><td>&nbsp;</td><td>92</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�����ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>0BS04921</td><td>����ϵͳʵ��</td><td>���޿�</td><td>&nbsp;</td><td>2.5</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>91</td><td>96</td><td>94</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�����ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>1BS15001</td><td>�����Ͷ�</td><td>���޿�</td><td>&nbsp;</td><td>1.0</td><td>   4.00</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>91</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>У���Ͷ�</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>1BH16001</td><td>ë��˼����й���ɫ�������������ϵ����</td><td>���޿�</td><td>&nbsp;</td><td>4.0</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>87</td><td>&nbsp;</td><td>94</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�������۽���ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>0BH04226</td><td>������Լ���</td><td>���޿�</td><td>&nbsp;</td><td>2</td><td>   4.00</td><td>98</td><td>&nbsp;</td><td>89</td><td>98</td><td>92</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�����ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>0BH04926</td><td>�������</td><td>���޿�</td><td>&nbsp;</td><td>3.0</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>87</td><td>98.4</td><td>93</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�����ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>0RH04214</td><td>���ݿⰲȫ</td><td>ѡ�޿�</td><td>&nbsp;</td><td>2.0</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>92</td><td>100</td><td>96</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�����ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr>
		<td>2016-2017</td><td>1</td><td>0BS04228</td><td>�ƶ�Ӧ�ÿ���ʵ��</td><td>���޿�</td><td>&nbsp;</td><td>2.0</td><td>   4.00</td><td>100</td><td>&nbsp;</td><td>&nbsp;</td><td>100</td><td>100</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�����ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr><tr class="alt">
		<td>2016-2017</td><td>1</td><td>0RH04221</td><td>�м������</td><td>ѡ�޿�</td><td>&nbsp;</td><td>2.0</td><td>   3.00</td><td>90</td><td>&nbsp;</td><td>83</td><td>85</td><td>85</td><td>0</td><td>&nbsp;</td><td>&nbsp;</td><td>�����ѧԺ</td><td>&nbsp;</td><td>0</td><td></td>
	</tr>
</table>
'''

if_match = re.findall(r'(<td>(.*)</td>){3}<td>(.*)</td><td>(.*)</td><td>&nbsp;</td>(<td>(.*)</td>){6}<td>([0-9]*)</td><td>0</td>', sample)
for i in if_match:
	print i



