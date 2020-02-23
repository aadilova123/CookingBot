import { Component, OnInit,Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Women }         from '../women';

import { WServiceService }  from '../wservice.service';

@Component({
  selector: 'app-w-detail',
  templateUrl: './w-detail.component.html',
  styleUrls: ['./w-detail.component.css']
})
export class WDetailComponent implements OnInit {
  @Input() women: Women;
  constructor(
    private route: ActivatedRoute,
    private Wservice: WServiceService,
    private location: Location
  ) { }

  ngOnInit(): void {
    this.getWomen();
  }

  getWomen(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.Wservice.getWomen(id)
      .subscribe(women => this.women = women);
  }

  goBack(): void {
    this.location.back();
  }

 save(): void {
    this.Wservice.updateWomen(this.women)
      .subscribe(() => this.goBack());
  }

}