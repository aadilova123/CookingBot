import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {ProductService} from '../product.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  product: any;

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
  ) {}

  ngOnInit() {
    this.getProduct();
  }

  getProduct() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id).subscribe(product => this.product = product);
  }

  zoomIn(id) {
    const main = document.getElementById('main') as HTMLImageElement;
    const need = document.getElementById(id) as HTMLImageElement;
    main.src = need.src;
  }

  zoomOut(id) {
    const main = document.getElementById('main') as HTMLImageElement;
    const need = document.getElementById('1') as HTMLImageElement;
    main.src = need.src;
  }

  Share() {
    window.open(this.product.link);
  }



}
