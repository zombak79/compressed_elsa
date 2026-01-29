gb_main = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
overflow:hidden;padding:2px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-danf{font-family:inherit;text-align:center;vertical-align:bottom}
.tg .tg-63ml{font-family:inherit;text-align:left;vertical-align:bottom}
.tg .tg-ezzy{font-family:inherit;text-align:right;vertical-align:bottom}
.tg .tg-ql1e{font-family:inherit;font-weight:bold;text-align:center;
vertical-align:bottom}
.tg .tg-kwi4{font-family:inherit;font-weight:bold;text-align:left;
vertical-align:bottom}
.tg .tg-904y{font-family:inherit;font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-47e0{font-family:inherit;font-style:italic;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-t9d2{font-family:inherit;text-align:right;vertical-align:bottom}
.tg .tg-uext{font-family:inherit;font-style:italic;font-weight:bold;text-align:left;vertical-align:bottom}
</style>
<table class="tg"><thead>
<tr>
    <th class="tg-kwi4"><span style="font-weight:bold">Model</span></th>
    <th class="tg-kwi4"><span style="font-weight:bold">Compression</span></th>
    <th class="tg-ql1e" colspan="5">Recall@20</th>
    <th class="tg-ql1e" colspan="5">Recall@50</th>
    <th class="tg-ql1e" colspan="5">NDCG@100</th>
</tr></thead>
<tbody>
<tr>
    <td class="tg-63ml">EASE</td>
    <td class="tg-63ml">None, factors=10000 (40000 B)</td>
    <td class="tg-danf" colspan="5">0.337</td>
    <td class="tg-danf" colspan="5">0.483</td>
    <td class="tg-danf" colspan="5">0.482</td>
</tr>
<tr>
    <td class="tg-63ml">ELSA</td>
    <td class="tg-63ml">None, factors=3250 (13000 B)</td>
    <td class="tg-danf" colspan="5">0.350</td>
    <td class="tg-danf" colspan="5">0.489</td>
    <td class="tg-danf" colspan="5">0.489</td>
</tr>
<tr>
    <td class="tg-63ml"></td>
    <td class="tg-904y"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-47e0"><span style="font-weight:bold;font-style:italic">64</span></td>
</tr>
<tr>
    <td class="tg-63ml">EASE</td>
    <td class="tg-63ml">Pruning (sparse)</td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.334</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.332</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.331</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.329</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.323</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.478</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.475</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.473</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.469</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.459</span></td>
    <td class="tg-t9d2">0.478</td>
    <td class="tg-t9d2">0.475</td>
    <td class="tg-t9d2">0.473</td>
    <td class="tg-t9d2">0.469</td>
    <td class="tg-t9d2">0.458</td>
</tr>
<tr>
    <td class="tg-63ml">ELSA</td>
    <td class="tg-63ml">Low dimensional training (dense)</td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.291</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.259</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.227</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.198</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.167</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.441</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.406</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.366</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.324</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.281</span></td>
    <td class="tg-t9d2">0.433</td>
    <td class="tg-t9d2">0.397</td>
    <td class="tg-t9d2">0.357</td>
    <td class="tg-t9d2">0.316</td>
    <td class="tg-t9d2">0.270</td>
</tr>
<tr>
    <td class="tg-63ml">ELSA</td>
    <td class="tg-63ml">Sparse projection post training</td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.309</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.304</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.299</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.295</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.291</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.439</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.432</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.424</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.418</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.413</span></td>
    <td class="tg-t9d2">0.436</td>
    <td class="tg-t9d2">0.428</td>
    <td class="tg-t9d2">0.420</td>
    <td class="tg-t9d2">0.413</td>
    <td class="tg-t9d2">0.408</td>
</tr>
<tr>
    <td class="tg-63ml">ELSA</td>
    <td class="tg-uext"><span style="font-weight:bold;font-style:italic">Sparse training (ours)</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.348</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.346</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.343</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.339</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.333</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.493</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.484</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.477</span></td>
    <td class="tg-t9d2"><span style="font-weight:normal">0.467</span></td>
    <td class="tg-t9d2">0.491</td>
    <td class="tg-t9d2">0.488</td>
    <td class="tg-t9d2">0.483</td>
    <td class="tg-t9d2">0.477</td>
    <td class="tg-t9d2">0.469</td>
</tr>
</tbody></table>"""

gb_pruning_strategy = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
overflow:hidden;padding:2px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-njgq{font-style:italic;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-dne1{text-align:left;vertical-align:bottom}
.tg .tg-fq8o{font-weight:bold;text-align:center;vertical-align:bottom}
.tg .tg-j6zm{font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
.tg .tg-2hz0{text-align:right;vertical-align:bottom}
</style>
<table class="tg"><thead>
<tr>
    <th class="tg-dne1"></th>
    <th class="tg-fq8o" colspan="5">Recall@20</th>
    <th class="tg-fq8o" colspan="5">Recall@50</th>
    <th class="tg-fq8o" colspan="5">NDCG@100</th>
</tr></thead>
<tbody>
<tr>
    <td class="tg-j6zm"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
</tr>
<tr>
    <td class="tg-7zrl">Exponential with restarting</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.348</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.346</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.343</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.339</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.333</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.493</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.484</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.477</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.467</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.491</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.488</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.483</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.477</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.469</span></td>
</tr>
<tr>
    <td class="tg-7zrl">Exponential</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.348</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.345</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.340</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.335</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.330</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.491</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.488</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.483</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.477</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.467</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.490</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.487</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.481</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.475</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.466</span></td>
</tr>
<tr>
    <td class="tg-7zrl">Linear with restarting</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.347</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.345</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.341</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.337</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.329</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.491</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.488</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.481</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.474</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.463</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.490</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.486</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.481</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.475</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.464</span></td>
</tr>
<tr>
    <td class="tg-7zrl">Linear</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.345</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.342</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.337</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.331</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.324</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.488</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.484</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.479</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.471</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.460</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.486</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.482</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.475</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.464</span></td>
</tr>
<tr>
    <td class="tg-7zrl">Step-wise with restarting</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.347</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.345</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.342</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.338</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.330</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.490</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.487</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.482</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.476</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.467</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.486</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.482</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.475</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.464</span></td>
</tr>
<tr>
    <td class="tg-7zrl">Step-wise</td>
    <td class="tg-2hz0">0.348</td>
    <td class="tg-2hz0">0.344</td>
    <td class="tg-2hz0">0.340</td>
    <td class="tg-2hz0">0.335</td>
    <td class="tg-2hz0">0.330</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.486</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.480</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.469</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.450</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.415</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.486</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.481</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.474</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.465</span></td>
</tr>
<tr>
    <td class="tg-7zrl">Constant</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.343</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.339</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.332</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.319</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.294</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.486</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.480</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.469</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.450</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.415</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.485</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.479</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.469</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.452</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.421</span></td>
</tr>
</tbody></table>"""

gb_factors = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
  font-weight:normal;overflow:hidden;padding:2px 5px;word-break:normal;}
.tg .tg-8rs4{text-align:right;vertical-align:bottom}
.tg .tg-njgq{font-style:italic;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-11x7{text-align:left;vertical-align:bottom}
.tg .tg-imct{font-weight:bold;text-align:center;vertical-align:bottom}
.tg .tg-j6zm{font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-11x7"></th>
    <th class="tg-imct" colspan="5">Recall@20</th>
    <th class="tg-imct" colspan="5">Recall@50</th>
    <th class="tg-imct" colspan="5">NDCG@100</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-j6zm"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">64 kB (8192 factors)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.349</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.347</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.344</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.339</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.332</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.492</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.484</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.478</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.466</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.491</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.485</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.479</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.469</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">48 kB (6144 factors)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.350</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.347</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.344</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.340</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.333</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.493</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.490</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.485</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.478</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.468</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.492</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.485</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.480</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.470</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">32 kB (4096 factors)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.348</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.346</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.343</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.339</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.333</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.493</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.489</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.484</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.477</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.467</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.491</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.488</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.483</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.477</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.469</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">16 kB (2048 factors)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.338</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.335</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.330</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.323</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.312</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.484</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.480</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.473</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.463</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.444</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.481</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.476</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.469</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.459</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.442</span></td>
  </tr>
</tbody></table>"""


ml_main = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
  overflow:hidden;padding:2px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-g6yg{font-family:inherit;text-align:center;vertical-align:bottom}
.tg .tg-t0a7{font-family:inherit;font-style:italic;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-x789{font-family:inherit;font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-fcnt{font-family:inherit;font-weight:bold;text-align:center;vertical-align:bottom}
.tg .tg-nf86{font-family:inherit;text-align:left;vertical-align:bottom}
.tg .tg-802b{font-family:inherit;text-align:right;vertical-align:bottom}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-x789"><span style="font-weight:bold">Model</span></th>
    <th class="tg-x789"><span style="font-weight:bold">Compression</span></th>
    <th class="tg-fcnt" colspan="5">Recall@20</th>
    <th class="tg-fcnt" colspan="5">Recall@50</th>
    <th class="tg-fcnt" colspan="5">NDCG@100</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-nf86">EASE</td>
    <td class="tg-nf86">None, factors=20720 (82880 B)</td>
    <td class="tg-g6yg" colspan="5">0.387</td>
    <td class="tg-g6yg" colspan="5">0.516</td>
    <td class="tg-g6yg" colspan="5">0.425</td>
  </tr>
  <tr>
    <td class="tg-nf86">ELSA</td>
    <td class="tg-nf86">None, factors=800 (3200 B)</td>
    <td class="tg-g6yg" colspan="5">0.393</td>
    <td class="tg-g6yg" colspan="5">0.528</td>
    <td class="tg-g6yg" colspan="5">0.429</td>
  </tr>
  <tr>
    <td class="tg-nf86"></td>
    <td class="tg-x789"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-t0a7"><span style="font-weight:bold;font-style:italic">64</span></td>
  </tr>
  <tr>
    <td class="tg-nf86">EASE</td>
    <td class="tg-nf86">Pruning (sparse)</td>
    <td class="tg-802b"><span style="font-weight:normal">0.382</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.377</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.368</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.354</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.335</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.507</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.499</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.486</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.469</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.442</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.419</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.414</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.404</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.391</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.368</span></td>
  </tr>
  <tr>
    <td class="tg-nf86">ELSA</td>
    <td class="tg-nf86">Low dimensional training (dense)</td>
    <td class="tg-802b"><span style="font-weight:normal">0.384</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.374</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.359</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.337</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.306</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.523</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.513</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.498</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.474</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.442</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.420</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.410</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.394</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.371</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.339</span></td>
  </tr>
  <tr>
    <td class="tg-nf86">ELSA</td>
    <td class="tg-nf86">Sparse projection post training</td>
    <td class="tg-802b"><span style="font-weight:normal">0.358</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.351</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.346</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.337</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.322</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.488</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.481</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.475</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.464</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.446</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.391</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.383</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.378</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.368</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.353</span></td>
  </tr>
  <tr>
    <td class="tg-nf86">ELSA</td>
    <td class="tg-nf86">Sparse training (ours)</td>
    <td class="tg-802b"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.384</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.375</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.363</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.344</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.522</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.515</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.504</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.487</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.462</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.425</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.420</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.411</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.398</span></td>
    <td class="tg-802b"><span style="font-weight:normal">0.378</span></td>
  </tr>
</tbody></table>"""

ml_pruning_strategy = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
  overflow:hidden;padding:2px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-8rs4{text-align:right;vertical-align:bottom}
.tg .tg-bobw{font-weight:bold;text-align:center;vertical-align:bottom}
.tg .tg-njgq{font-style:italic;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
.tg .tg-j6zm{font-weight:bold;text-align:left;vertical-align:bottom}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-7zrl"></th>
    <th class="tg-bobw" colspan="5">Recall@20</th>
    <th class="tg-bobw" colspan="5">Recall@50</th>
    <th class="tg-bobw" colspan="5">NDCG@100</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-j6zm"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Exponential with restarting</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.384</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.375</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.363</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.344</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.522</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.515</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.504</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.487</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.462</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.425</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.420</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.411</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.398</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.378</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Exponential</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.387</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.381</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.372</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.360</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.341</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.519</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.511</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.499</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.483</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.458</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.424</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.418</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.408</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.395</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.375</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Linear with restarting</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.383</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.372</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.358</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.333</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.522</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.515</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.500</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.480</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.449</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.426</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.420</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.408</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.392</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.366</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Linear</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.386</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.380</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.371</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.359</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.341</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.518</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.510</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.498</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.482</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.458</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.423</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.417</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.407</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.393</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.375</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Step-wise with restarting</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.386</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.379</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.369</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.354</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.331</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.517</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.508</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.495</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.476</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.446</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.421</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.415</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.404</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.365</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Step-wise</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.386</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.380</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.371</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.359</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.340</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.518</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.510</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.498</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.482</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.457</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.422</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.416</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.406</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.394</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.373</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Constant</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.385</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.376</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.365</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.350</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.323</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.518</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.506</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.491</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.471</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.436</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.422</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.413</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.401</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.386</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.357</span></td>
  </tr>
</tbody></table>"""

ml_factors = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
  overflow:hidden;padding:2px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-njgq{font-style:italic;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-0xmo{;text-align:right;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
.tg .tg-8d8j{text-align:center;vertical-align:bottom}
.tg .tg-j6zm{font-weight:bold;text-align:left;vertical-align:bottom}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-7zrl"></th>
    <th class="tg-8d8j" colspan="5">Recall@20</th>
    <th class="tg-8d8j" colspan="5">Recall@50</th>
    <th class="tg-8d8j" colspan="5">NDCG@100</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-j6zm"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">64 kB (8192 factors)</td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.386</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.380</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.370</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.356</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.333</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.517</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.509</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.495</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.478</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.448</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.386</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.380</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.370</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.356</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.333</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">48 kB (6144 factors)</td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.388</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.382</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.373</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.360</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.340</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.520</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.513</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.500</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.482</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.456</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.388</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.382</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.373</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.360</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.340</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">32 kB (4096 factors)</td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.389</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.384</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.375</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.363</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.344</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.522</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.515</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.504</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.487</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.462</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.389</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.384</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.375</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.363</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.344</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">16 kB (2048 factors)</td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.384</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.376</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.364</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.345</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.313</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.517</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.507</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.489</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.464</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.423</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.384</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.376</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.364</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.345</span></td>
    <td class="tg-0xmo"><span style="font-weight:normal;">0.313</span></td>
  </tr>
</tbody></table>"""


netflix_main = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
  overflow:hidden;padding:2px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-8rs4{text-align:right;vertical-align:bottom}
.tg .tg-im9u{font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-bobw{font-weight:bold;text-align:center;vertical-align:bottom}
.tg .tg-wi06{font-style:italic;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-j6zm{font-weight:bold;text-align:left;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
.tg .tg-8d8j{text-align:center;vertical-align:bottom}
.tg .tg-u4kt{text-align:left;vertical-align:bottom}
.tg .tg-o3q7{text-align:center;vertical-align:bottom}
.tg .tg-ffcf{font-style:italic;font-weight:bold;text-align:left;vertical-align:bottom}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-j6zm"><span style="font-weight:bold">Model</span></th>
    <th class="tg-j6zm"><span style="font-weight:bold">Compression</span></th>
    <th class="tg-bobw" colspan="5"><span style="font-weight:bold">Recall@20</span></th>
    <th class="tg-bobw" colspan="5"><span style="font-weight:bold">Recall@50</span></th>
    <th class="tg-bobw" colspan="5"><span style="font-weight:bold">NDCG@100</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-7zrl">EASE</td>
    <td class="tg-7zrl">None, factors=17769 (71076 B)</td>
    <td class="tg-8d8j" colspan="5">0.354</td>
    <td class="tg-8d8j" colspan="5">0.441</td>
    <td class="tg-8d8j" colspan="5">0.395</td>
  </tr>
  <tr>
    <td class="tg-u4kt">ELSA</td>
    <td class="tg-u4kt">None, factors=2450 (9800 B)</td>
    <td class="tg-o3q7" colspan="5">0.353</td>
    <td class="tg-o3q7" colspan="5">0.441</td>
    <td class="tg-o3q7" colspan="5">0.394</td>
  </tr>
  <tr>
    <td class="tg-u4kt"></td>
    <td class="tg-im9u"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-wi06"><span style="font-weight:bold;font-style:italic">64</span></td>
  </tr>
  <tr>
    <td class="tg-u4kt">EASE</td>
    <td class="tg-u4kt">Pruning (sparse)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.349</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.344</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.337</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.326</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.307</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.435</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.429</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.420</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.407</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.381</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.384</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.377</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.365</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.343</span></td>
  </tr>
  <tr>
    <td class="tg-u4kt">ELSA</td>
    <td class="tg-u4kt">Low dimensional training (dense)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.333</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.321</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.306</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.288</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.266</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.427</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.415</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.399</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.379</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.355</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.376</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.364</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.349</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.330</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.307</span></td>
  </tr>
  <tr>
    <td class="tg-u4kt">ELSA</td>
    <td class="tg-u4kt">Sparse projection post training</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.297</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.287</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.282</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.276</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.270</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.391</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.381</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.376</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.370</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.362</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.341</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.331</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.326</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.320</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.314</span></td>
  </tr>
  <tr>
    <td class="tg-u4kt">ELSA</td>
    <td class="tg-ffcf"><span style="font-weight:bold;font-style:italic">Sparse training (ours)</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.351</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.347</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.341</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.332</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.317</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.440</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.434</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.428</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.416</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.397</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.393</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.382</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.373</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.357</span></td>
  </tr>
</tbody></table>"""

netflix_pruning_startegy = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
  overflow:hidden;padding:2px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
.tg .tg-2hz0{text-align:right;vertical-align:bottom}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-baqh" colspan="5"><span style="font-weight:bold">Recall@20</span></th>
    <th class="tg-baqh" colspan="5"><span style="font-weight:bold">Recall@50</span></th>
    <th class="tg-baqh" colspan="5"><span style="font-weight:bold">NDCG@100</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-0lax"><span style="font-weight:bold;font-style:italic">64</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">Exponential with restarting</td>
    <td class="tg-0lax"><span style="font-weight:normal">0.351</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.347</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.341</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.332</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.317</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.440</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.434</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.428</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.416</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.397</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.393</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.382</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.373</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.357</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Exponential</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.349</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.345</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.339</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.331</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.316</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.438</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.434</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.426</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.415</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.396</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.391</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.387</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.381</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.372</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.356</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Linear with restarting</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.349</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.345</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.337</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.327</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.309</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.439</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.434</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.423</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.410</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.388</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.391</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.387</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.379</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.368</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.349</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">Linear</td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.349</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.345</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.339</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.330</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.317</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.438</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.433</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.426</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.415</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.398</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.390</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.386</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.381</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.371</span></td>
    <td class="tg-2hz0"><span style="font-weight:normal">0.358</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">Step-wise with restarting</td>
    <td class="tg-0lax"><span style="font-weight:normal">0.348</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.344</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.338</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.327</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.309</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.436</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.431</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.423</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.410</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.387</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.390</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.386</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.379</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.368</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.349</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">Step-wise</td>
    <td class="tg-0lax"><span style="font-weight:normal">0.349</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.346</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.340</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.330</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.316</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.437</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.433</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.427</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.414</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.396</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.391</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.387</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.382</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.371</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.356</span></td>
  </tr>
  <tr>
    <td class="tg-0lax">Constant</td>
    <td class="tg-0lax"><span style="font-weight:normal">0.348</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.343</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.334</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.323</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.300</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.436</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.430</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.419</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.406</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.377</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.385</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.376</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.364</span></td>
    <td class="tg-0lax"><span style="font-weight:normal">0.341</span></td>
  </tr>
</tbody></table>"""

netflix_factors = """<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-size:14px;
  overflow:hidden;padding:2px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-8rs4{text-align:right;vertical-align:bottom}
.tg .tg-bobw{font-weight:bold;text-align:center;vertical-align:bottom}
.tg .tg-njgq{font-style:italic;font-weight:bold;text-align:right;vertical-align:bottom}
.tg .tg-7zrl{text-align:left;vertical-align:bottom}
.tg .tg-j6zm{font-weight:bold;text-align:left;vertical-align:bottom}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-7zrl"></th>
    <th class="tg-bobw" colspan="5">Recall@20</th>
    <th class="tg-bobw" colspan="5">Recall@50</th>
    <th class="tg-bobw" colspan="5">NDCG@100</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-j6zm"><span style="font-weight:bold">Vector size (bytes)</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">1024</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">512</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">256</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">128</span></td>
    <td class="tg-njgq"><span style="font-weight:bold;font-style:italic">64</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">64 kB (8192 factors)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.437</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.432</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.422</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.409</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.385</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.437</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.432</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.422</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.409</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.385</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.391</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.387</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.378</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.367</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.347</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">48 kB (6144 factors)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.439</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.434</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.426</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.413</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.393</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.439</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.434</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.426</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.413</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.393</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.392</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.388</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.381</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.370</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.353</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">32 kB (4096 factors)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.440</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.434</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.428</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.416</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.397</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.440</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.434</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.428</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.416</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.397</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.393</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.389</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.382</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.373</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.357</span></td>
  </tr>
  <tr>
    <td class="tg-7zrl">16 kB (2048 factors)</td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.436</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.429</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.417</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.399</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.367</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.436</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.429</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.417</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.399</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.367</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.387</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.381</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.372</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.357</span></td>
    <td class="tg-8rs4"><span style="font-weight:normal">0.329</span></td>
  </tr>
</tbody></table>"""