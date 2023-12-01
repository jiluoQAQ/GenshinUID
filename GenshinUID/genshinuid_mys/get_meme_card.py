# flake8: noqa
import random

from gsuid_core.utils.image.convert import convert_img
from gsuid_core.utils.image.image_tools import get_pic

title = 'https://webstatic.mihoyo.com/upload/event'
meme_dict = {
    'card_other_Fischl1': f'{title}/2020/08/31/4bb5924e073f073f400389da2062407f_4225300656656631729.png',
    'card_other_Fischl2': f'{title}/2020/08/31/9a477826d4587eaafa7161507e53cec1_3070825784718745991.png',
    'card_other_albedo1': f'{title}/2021/01/05/929f01ef0b7db16e6e3289e6f09bc664_3314543116725683931.png',
    'card_other_albedo2': f'{title}/2021/01/05/f486f444ebe67ebdb70307433aa08fd3_8750695094071258948.png',
    'card_other_ambor1': f'{title}/2020/08/31/997dca7a05c35b09881b19c08e265477_1299947423447392337.png',
    'card_other_ambor2': f'{title}/2020/08/31/0ad6dd1e9903507a659df257959a763f_2854888966169652134.png',
    'card_other_ambor3': f'{title}/2020/08/31/fd905e0fb575f67da73137b453a596fd_2915100968963816162.png',
    'card_other_bannite1': f'{title}/2020/08/31/9cefb9bd9811f166bf14b8367dc785df_3763750909505644121.png',
    'card_other_bannite2': f'{title}/2020/08/31/8d4d7f176808b85529d5e53f9ef59eb3_873542905371029363.png',
    'card_other_barbara1': f'{title}/2020/08/31/160b860e2968c0a930373bf74dbe34a6_6782336143409269316.png',
    'card_other_barbara2': f'{title}/2020/08/31/837fc37bd0831b74c0281c945d5323da_4271787076408799417.png',
    'card_other_barbara3': f'{title}/2020/08/31/ca72b6a24f48ef04796e3c63a7c25163_5778250222995475858.png',
    'card_other_beidou1': f'{title}/2020/08/31/15e08973b2d2896bb403f1f5f7499382_1462646223869539529.png',
    'card_other_beidou2': f'{title}/2020/08/31/b11c93805674e62fc43a9adceaa8e893_8926566513833977124.png',
    'card_other_chongyun1': f'{title}/2020/08/31/b9920d1400bf55a2307b9b2e216a4a8e_2000240380863580838.png',
    'card_other_chongyun2': f'{title}/2020/08/31/1f80b78033c55c31553d2fba2201c857_8778762270527512136.png',
    'card_other_chongyun3': f'{title}/2020/08/31/645cf32a7a133b57605bb341a84d65a2_7809384165096554836.png',
    'card_other_diaona1': f'{title}/2020/11/16/f975f0e6311346306e5151f04fbbbc0a_6762294099269212599.png',
    'card_other_diaona2': f'{title}/2020/11/16/0530db8dbacbebf662c3b4cad1f407c8_7326500760952263133.png',
    'card_other_diluc1': f'{title}/2020/08/31/4d25ea66387705c7360ea6d5cc90bb01_4560335127797724868.png',
    'card_other_diluc2': f'{title}/2020/08/31/378f274d1f40a840c14da114f97c689d_6631287774563316092.png',
    'card_other_ganyu1': f'{title}/2021/01/12/745fc70073f22a37bb0238a06a53cfdb_1162143275141578017.png',
    'card_other_ganyu2': f'{title}/2021/01/12/57f6fcf67cd8859c3a6ff32597d9c99a_3170022474475150543.png',
    'card_other_gongzi1': f'{title}/2020/11/16/40e0bc9a555fcbbbdfb74a95d2e387ef_8519449231927106780.png',
    'card_other_gongzi2': f'{title}/2020/11/16/04b40cd1a848577f9cde336a3039c750_3996605459102489069.png',
    'card_other_kaeya1': f'{title}/2020/08/31/e05c2fe7d9ab737a25285c060aab1aa0_2111907448530751567.png',
    'card_other_kaeya2': f'{title}/2020/08/31/9c1e67747a78b5e22ae3834814c57a8f_6116180424455008670.png',
    'card_other_keqing1': f'{title}/2020/08/31/1f62425cec6ffc21ecf4c8f0da499ac7_4928089850342437737.png',
    'card_other_keqing2': f'{title}/2020/08/31/3a6f0d284e2ab862c82ee3a07d6ffbc7_7794570330643971174.png',
    'card_other_klee1': f'{title}/2020/08/31/b120c4ac7c695d3aaf55441eb43600d1_4487729736509862376.png',
    'card_other_klee2': f'{title}/2020/08/31/08aa6011f26df790dbf2681678f1d7e9_2796140925707265189.png',
    'card_other_klee3': f'{title}/2020/08/31/c00aa8fa9d2cbf9edcccd50b457ae5a6_5422323085963273352.png',
    'card_other_leize1': f'{title}/2020/08/31/34bde2a566136897ab22932a9001d572_4843575850627066457.png',
    'card_other_leize2': f'{title}/2020/08/31/bd6894fa5c5daa833b4eede40cf01385_2519521084432177379.png',
    'card_other_lisa1': f'{title}/2020/08/31/c23a633e2eb72a10fb51198550d59a8a_542776791456547653.png',
    'card_other_lisa2': f'{title}/2020/08/31/a46cccf622c2d4dbff6c5353b936eee4_1652272197678612672.png',
    'card_other_mona1': f'{title}/2020/08/31/20ae5d9e7ea88ee27dd02208714e622e_2311908118844083107.png',
    'card_other_mona2': f'{title}/2020/08/31/da669761dcbd5c029bda0a62bccb301e_8046604345851128002.png',
    'card_other_ningguang1': f'{title}/2020/08/31/c11a5c5c90d54c98f10c6f257e8eac01_6529728627802398273.png',
    'card_other_ningguang2': f'{title}/2020/08/31/4165b7cb43e3369a279ccef46c295769_3879970605580805258.png',
    'card_other_nuoaier1': f'{title}/2020/08/31/3df9ee03bc4629e6e2af3c7225674543_2742734744870268629.png',
    'card_other_nuoaier2': f'{title}/2020/08/31/051cb060351937831252e395f65834c8_6289474038603880117.png',
    'card_other_qin1': f'{title}/2020/08/31/95c9ef420173047f635e963db2dae3f6_5948753857591750018.png',
    'card_other_qin2': f'{title}/2020/08/31/b45dd906708dbd5ceff7960bd48baab7_605993513095277023.png',
    'card_other_qiqi1': f'{title}/2020/08/31/b373e3bcb24285b96fd106747c9be482_2380875567755087743.png',
    'card_other_qiqi2': f'{title}/2020/08/31/e17547277f4dfb7bc96f764536b19406_3629575916992344590.png',
    'card_other_qiqi3': f'{title}/2020/08/31/58b24db38da079a9230e37d741b940c3_7709490267389090600.png',
    'card_other_shatang1': f'{title}/2020/08/31/315f96761caa9b22993180d529e6c935_169150677634938584.png',
    'card_other_shatang2': f'{title}/2020/08/31/e4a7ff004ee5d04678add5bb7c3c5fd9_506219715714537000.png',
    'card_other_venti1': f'{title}/2020/08/31/80905774b30aaa4b26a5b75926dcf7b3_222995534350028202.png',
    'card_other_venti2': f'{title}/2020/08/31/c75eb06e4d0b7856652c9893af2da63e_5411923475027982287.png',
    'card_other_xiangling1': f'{title}/2020/08/31/d19849df8be15bff53cdc0a0146f534a_1468443590902001424.png',
    'card_other_xiangling2': f'{title}/2020/08/31/a105a4aca30bdf8348519140736c306d_5118343542859881269.png',
    'card_other_xingqiu1': f'{title}/2020/09/27/ad7183031224452a2894b9516fd571ad_3529083730481381114.png',
    'card_other_xingqiu2': f'{title}/2020/09/27/1761487a5da1ea037be6ae80d24e1423_9220243684814419617.png',
    'card_zero_paimeng1': f'{title}/2020/08/31/a27f1224a0b149c684ecb3a1d3f7a4ec_2661825294156591596.png',
    'card_zero_paimeng2': f'{title}/2020/08/31/cb137a55d6527cd2cde1d0b47e13592f_4335931514300413032.png',
    'card_zero_paimeng3': f'{title}/2020/08/31/1231b4066fb103409b43466c61fa4e5c_7013106042012366406.png',
    'card_zero_qiu1': f'{title}/2020/08/31/dd329cd9e5980421bef3354e334d73a0_2484329576384567186.png',
    'card_zero_qiu2': f'{title}/2020/08/31/b3eb2286d9945c3caf695c3992bc93e2_4449302548761785968.png',
    'card_zero_qiu3': f'{title}/2020/08/31/7a15e33790ef2d513a5e6e7760cbc7be_8171554806202001370.png',
}


async def get_meme_img() -> bytes:
    url = random.choice(list(meme_dict.values()))
    data = await get_pic(url)
    return await convert_img(data)
