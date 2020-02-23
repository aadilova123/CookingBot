import { Component, OnInit } from '@angular/core';

import { Women } from '../women';
import { WServiceService } from '../wservice.service';

@Component({
  selector: 'app-woman',
  templateUrl: './woman.component.html',
  styleUrls: ['./woman.component.css']
})

export class WomanComponent implements OnInit {
  woman: Women[];
  constructor(private Wservice: WServiceService) { }

  ngOnInit(): void {
    this.getListW();
  }

  getListW(): void {
    this.Wservice.getListW()
    .subscribe(woman => this.woman = woman);
  }

  add(name: string): void {
    name = name.trim();
    if (!name) { return; }
    this.Wservice.addHero({ name } as Women)
      .subscribe(women => {
        this.woman.push(women);
      });
  }

  delete(women: Women): void {
    this.woman = this.woman.filter(h => h !== women);
    this.Wservice.deleteWomen(women).subscribe();
  }

}


