const biller = document.getElementById("biller");
const paymentItem = document.getElementById("payment-item");

let changeValue = () => {
    if (biller.value == "select-biller") {
        paymentItem.innerHTML = `<option value="payment">Payment item</option>`
    } else if (biller.value == "gotv") {
        paymentItem.innerHTML = `
        <option value="datavalue ">Jinja- Monthly (N1,900.00)</option>
        <option value="datavalue ">Jolli- Monthly (N2,800.00)</option>
        <option value="datavalue ">Max- Monthly (N4,150.00)</option>
        <option value="datavalue ">Smallie- Monthly (N900.00)</option>
        <option value="datavalue ">SUPA- Monthly (N1,900.00)</option>
        <option value="datavalue ">Smallie- Quarterly (N2,400.00)</option>
        <option value="datavalue ">Smallie- Annually (N7,000.00)</option>
        <option value="datavalue ">Jinja- 4 Months (N7,600.00)</option>
        <option value="datavalue ">Jinja- 12 Months (N22,800.00)</option>
        <option value="datavalue ">Jolli- 4 Months (N2,000.00)</option>
        <option value="datavalue ">Jolli- 12 Months (N33,600.00)</option>
        <option value="datavalue ">Max- 4 Month (N16,600.00)</option>
        <option value="datavalue ">Max- 12 Months (N49,800.00)</option>
        <option value="datavalue ">GOTV RENEW- (Fill Amount)</option>
        <option value="datavalue ">GOTV TOP UP- (Fill Amount)</option>
        `
    } else if (biller.value == "startimes") {
        paymentItem.innerHTML = `
        <option value="datavalue ">Basic (Antena) - Weekly (N550.00)</option>
        <option value="datavalue ">Basic (Antena) - Monthly (N1,700.00)</option>
        <option value="datavalue ">Classic (Antena) - Weekly (N1,150.00)</option>
        <option value="datavalue ">Classic (Antena) - Monthly (N2,500.00)</option>
        <option value="datavalue ">Nova (Antena) - Weekly (N300.00)</option>
        <option value="datavalue ">Nova (Antena) - Monthly (N900.00)</option>
        <option value="datavalue ">Solar-Nova - Monthly (N9,900.00)</option>
        <option value="datavalue ">Solar-Smart - Monthly (N10,500.00)</option>
        <option value="datavalue ">Solar-Super - Monthly (N11,400.00)</option>
        <option value="datavalue ">Smart (Dish) - Weekly (N700.00)</option>
        <option value="datavalue ">Smart (Dish) - Monthly (N2,600.00)</option>
        <option value="datavalue ">Super (Dish) - Weekly (N1,500.00)</option>
        <option value="datavalue ">Super (Dish) - Monthly (N4,900.00)</option>
        <option value="datavalue ">Nova (Dish) - Weekly (N300.00)</option>
        <option value="datavalue ">Nova (Dish) - Monthly (N900.00)</option>
        <option value="datavalue ">Startimes All inclusive - Monthly (N12,000.00)</option>
        <option value="datavalue ">Startimes Renew - (Fill Amount)</option>
        `
    } else if (biller.value == "DSTV") {
        paymentItem.innerHTML = `
        <option value="datavalue ">Padi - Monthly (N2,150.00)</option>
        <option value="datavalue ">Yanga - Monthly (N2,950.00)</option>
        <option value="datavalue ">Confam - Monthly (N5,300.00)</option>
        <option value="datavalue ">Compact - Monthly (N9,000.00)</option>
        <option value="datavalue ">Compact Plus - Monthly (N14,250.00)</option>
        <option value="datavalue ">Premium (N21,000.00)</option>
        <option value="datavalue ">Business (N2,66g)</option>
        <option value="datavalue ">Xtraview + PVR Access (N2,900.00)</option>
        <option value="datavalue ">DSTV RENEW (Fill Amount)</option>
          `
    } else if (biller.value == "Box-DSTV") {
        paymentItem.innerHTML = `
        <option value="datavalue ">Box Office Wallet Topup (Fill Amount)</option>
          `
    }

    else if (biller.value == "SHOWMAX") {
        paymentItem.innerHTML = `
        <option value="datavalue ">Showmax Mobile - Monthly (N1,200.00)</option>
        <option value="datavalue ">Pro Mobile - Monthly (N3,200.00)</option>
        <option value="datavalue ">Showmax Pro - Monthly (N6,300.00)</option>
        <option value="datavalue ">Showmax - Monthly (N2,900.00)</option>
         `
    }

    else if (biller.value == "IROKOtv") {
        paymentItem.innerHTML = `
        <option value="datavalue ">IROKOtv Plus Web Access (N800.00)</option>
          `
    }
    else if (biller.value == "Linda-TV") {
        paymentItem.innerHTML = `
        <option value="datavalue ">1 Month (N1,000.00)</option>
        <option value="datavalue ">3 Month (N3,000.00)</option>
        <option value="datavalue ">6 Month (N5,500.00)</option>
        <option value="datavalue ">12 Month (N10,000.00)</option>
          `
    }

}

biller.addEventListener("change", changeValue);