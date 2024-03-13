import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = [...products];

  share(link: string) {
    const shareMessage = `Product:  ${link}`;
    const telegramLink = `https://t.me/share/url?url=${encodeURIComponent(shareMessage)}`;
    window.location.href = telegramLink;
  }

  share_whatsapp(link: string){
    window.location.href = "https://web.whatsapp.com/"
  }

  share_kaspi(link: string){
    const kaspiLink = `${link}`;
    window.open(kaspiLink);

  }
}